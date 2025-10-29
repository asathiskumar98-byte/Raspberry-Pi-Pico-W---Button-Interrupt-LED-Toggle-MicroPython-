# Raspberry Pi Pico W - Button Interrupt LED Toggle (MicroPython)

This project demonstrates using **hardware interrupts** on the Raspberry Pi Pico W to toggle the on-board LED when a push button is pressed.

## 🧰 Requirements
- Raspberry Pi Pico / Pico W
- Thonny IDE
- MicroPython Firmware

## ⚙️ Pin Configuration
| Component | Pin | Description |
|------------|-----|-------------|
| LED | On-board | GPIO 25 |
| Push Button | GP16 | Input with Pull-up |

## 🧩 Working Principle
- The button press triggers a **falling-edge interrupt**.
- The interrupt service routine toggles the LED.
- Debounce delay ensures stable operation.

## 🧠 Code Highlights
- Uses `irq()` method for interrupt handling.
- Simple debounce using `time.sleep()`.
- Fully compatible with Pico and Pico W.
