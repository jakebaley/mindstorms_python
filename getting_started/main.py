#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

motors = Motor(Port.B)
sensor = InfraredSensor(Port.S3)
shooter = Motor(Port.D)

target = 180
# Write your program here.
ev3.speaker.beep()
while True:

    if (sensor.distance() <= 15):

        # ev3.speaker.set_speech_options(voice='f2', speed=0.5)
        # ev3.speaker.set_volume(100)
        # ev3.speaker.say('UPGRADED TORO. CHARGE')

        # motors.run_target(500,target)
        target = target + 180
        shooter.run_angle(500, -300)
        shooter.run_angle(500, 300)