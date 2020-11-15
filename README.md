"""Wi-Fi signal strength LED indicator. WEMOS D1 mini project"""

LED indicator visually shows you the received signal strength RSSI in dBm from a Wi-Fi router.
The indicator is implemented using three LEDs: 
- green LED is used to indicate a good signal strength (-60...0 dBm),
- yellow LED is used to indicate a medium signal strength (-75...-61 dBm),
- red LED indicates a poor received signal strength ( < -75 dBm).

Parts:
- Wemos D1 mini on esp8266 board,
- 3 LEDs (red, yellow and green),
- Resistor 330R,
- Breadboard,
- Wires.