#
# SerialLightControl-Server.py - This is the code to complete
# Milestone Two.
#
# This Python code will be used to control the light in the circuit
# that you built on your solderless breadboard in Milestone One based
# on the instructions read from the serial port of your Raspberry pi.
#
# This script requires that you have correctly configured your Serial
# port and have a USB -> TTL cable connected appropriately.
#
#------------------------------------------------------------------
# Change History
#------------------------------------------------------------------
# Version   |   Description
#------------------------------------------------------------------
#    1          Initial Development
#------------------------------------------------------------------

import serial
import RPi.GPIO as GPIO

ser = serial.Serial(
        port='/dev/ttyS0',
        baudrate=115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

repeat = True

while repeat:
        try:
                command = (ser.readline().decode("utf-8")).strip().lower()

                match command:
                        case "off":
                                GPIO.output(18, GPIO.LOW)

                        case "on":
                                GPIO.output(18, GPIO.HIGH)

                        case "exit" | "quit":
                                GPIO.output(18, GPIO.LOW)
                                GPIO.cleanup()
                                repeat = False

                        case _:
                                pass

        except KeyboardInterrupt:
                GPIO.output(18, GPIO.LOW)
                GPIO.cleanup()
                repeat = False
