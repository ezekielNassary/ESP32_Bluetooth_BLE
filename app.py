from machine import Pin, SoftI2C
from time import sleep_ms
from ble import BLE

class App:
    def __init__(self):
        self.i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
        self.red_led = Pin(2, Pin.OUT)
        self.ble = BLE("ESP32")
        self.run()

    def run(self):
        while True:
            sleep_ms(100)  # Just to keep the loop running


if __name__ == "__main__":
    app = App()
