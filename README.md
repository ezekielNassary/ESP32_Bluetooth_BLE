# ESP32_Bluetooth_BLE

Integrate Bluetooth with your ESP32 easily. Follow the instructions below to set up the firmware and run the provided scripts.

## Firmware Installation

1. Download the latest firmware for ESP32 from [here](https://micropython.org/download/ESP32_GENERIC/).
2. Follow the instructions on the page to flash the firmware onto your ESP32.


## Description

This project demonstrates how to integrate Bluetooth functionality into an ESP32 using MicroPython. It includes:

- A `BLE` class to handle Bluetooth Low Energy (BLE) operations.
- An `App` class to run the main application logic, including pin interrupts and Watchdog Timer (WDT) integration.

## Setup

1. Ensure you have the latest MicroPython firmware installed on your ESP32.
2. Copy `ble.py` and `app.py` to your ESP32 device.
3. Run `app.py` to start the application.

## Files

### ble.py

This file contains the `BLE` class, which handles Bluetooth operations such as advertising, connecting, disconnecting, and receiving messages.

### app.py

This file contains the `App` class, which:
- Initializes the I2C interface.
- Sets up the BLE functionality.
- Configures a pin interrupt on pin 18.
- Integrates a Watchdog Timer (WDT) to reset the system in case of hangs.

### Example Usage

To use the `App` class, simply run `app.py` on your ESP32. The application will:
- Advertise the ESP32 over Bluetooth.
- Handle connections and disconnections.
- Process incoming messages to control an LED or read sensor data.
- Use the WDT to enhance system reliability.

## Requirements

- ESP32 board
- MicroPython firmware (latest version)
- HDC1080 sensor (optional, for temperature and humidity readings)

## Running the Project

1. Copy the `ble.py` and `app.py` files to your ESP32.
2. Use a serial terminal to run `app.py`.
3. The ESP32 will start advertising over Bluetooth. You can connect to it using a Bluetooth-capable device.

## Troubleshooting

- Ensure the latest MicroPython firmware is installed.
- Check the wiring and connections of your ESP32 and any connected sensors.
- Monitor the serial output for any error messages and debug accordingly.

## License

This project is licensed under the MIT License.

## Contributions

Contributions are welcome! Please fork this repository and submit pull requests.

## Support

If you have any questions or need help, feel free to open an issue on GitHub.


