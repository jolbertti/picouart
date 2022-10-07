from machine import UART, Pin
from time import sleep_us

uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1), bits=8, parity=None, stop=1)

uart.write("AT\r\n") # returns OK if it works - search AT commands for more
sleep_us(100000)
print(uart.read())
