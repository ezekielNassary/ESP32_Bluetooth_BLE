# ble.py

from machine import Pin, Timer
from time import sleep_ms
import ubluetooth

class BLE():
    def __init__(self, name):
        self.name = name
        self.ble = ubluetooth.BLE()
        self.ble.active(True)

        self.led = Pin(2, Pin.OUT)
        self.timer1 = Timer(0)
        self.timer2 = Timer(1)

        self.disconnected()
        self.ble.irq(self.ble_irq)
        self.register()
        self.advertiser()

    def connected(self):
        self.timer1.deinit()
        self.timer2.deinit()
        print("Device connected")

    def disconnected(self):
        self.timer1.init(period=1000, mode=Timer.PERIODIC,
                         callback=lambda t: self.led.value(1))
        sleep_ms(200)
        self.timer2.init(period=1000, mode=Timer.PERIODIC,
                         callback=lambda t: self.led.value(0))
        print("Device disconnected")

    def ble_irq(self, event, data):
        if event == 1:
            '''Central connected'''
            self.connected()
            self.led.value(1)

        elif event == 2:
            '''Central disconnected'''
            self.advertiser()
            self.disconnected()

        elif event == 3:
            '''New message received'''
            buffer = self.ble.gatts_read(self.rx)
            message = buffer.decode('UTF-8').strip()
            print(f"Received message: {message}")
            if message == 'red_led':
                red_led.value(not red_led.value())
                print(f"Red LED toggled to {red_led.value()}")
                self.send('red_led ' + str(red_led.value()))
            elif message == 'read_temp':
                temp = sensor.read_temperature(True)
                print(f"Temperature: {temp}")
                self.send(f"Temperature: {temp}")
            elif message == 'read_hum':
                hum = sensor.read_humidity()
                print(f"Humidity: {hum}")
                self.send(f"Humidity: {hum}")

    def register(self):
        # Nordic UART Service (NUS)
        NUS_UUID = '6E400001-B5A3-F393-E0A9-E50E24DCCA9E'
        RX_UUID = '6E400002-B5A3-F393-E0A9-E50E24DCCA9E'
        TX_UUID = '6E400003-B5A3-F393-E0A9-E50E24DCCA9E'

        BLE_NUS = ubluetooth.UUID(NUS_UUID)
        BLE_RX = (ubluetooth.UUID(RX_UUID), ubluetooth.FLAG_WRITE)
        BLE_TX = (ubluetooth.UUID(TX_UUID), ubluetooth.FLAG_NOTIFY)

        BLE_UART = (BLE_NUS, (BLE_TX, BLE_RX,))
        SERVICES = (BLE_UART, )
        ((self.tx, self.rx,), ) = self.ble.gatts_register_services(SERVICES)

    def send(self, data):
        self.ble.gatts_notify(0, self.tx, data + '\n')

    def advertiser(self):
        name = bytes(self.name, 'UTF-8')
        adv_data = b'\x02\x01\x06' + bytes((len(name) + 1,)) + b'\x09' + name
        self.ble.gap_advertise(100, adv_data)
