#!/usr/bin/env python
# Simply prints the state of the obstacle sensors

# Must be run as root - sudo python .py

import time, pi2go

pi2go.init()

try:
    # Pseudocode for robot
    # It has 3 sensors
    # Need to run IR Test

    # Ultimate goal is to go forward

    from pi2go import *


    # Bools for if obstacle on each way
    # Drive my robot forwards - this should be a function
    def update_degrees(num):
        """
        :param num: The num to add to degrees
        :return:
        """
        global degrees
        degrees = (degrees + num) % 360


    # Set sleep timer for reading sensors
    degrees = 0
    speed = 70
    counter = -1
    # Set it forever
    while True:
        # Get Information - True
        left = irLeft()
        right = irRight()
        center = irCentre()

        # If forwards is free go forward
        if not center and not left and not right:
            # Every 2 seconds
            if counter % 20 == 0:
                # Turn towards the left
                spinLeft(70)
                time.sleep(0.3)

            forward(speed)

        time.sleep(0.5)


except KeyboardInterrupt:
    print

finally:
    pi2go.cleanup()
