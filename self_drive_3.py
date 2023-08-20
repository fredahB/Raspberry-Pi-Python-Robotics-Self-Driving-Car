#!/usr/bin/env python
# Simply prints the state of the obstacle sensors

# Must be run as root - sudo python .py

import time, pi2go

pi2go.init()

try:
    while True:
        left = pi2go.irLeft()
        center = pi2go.irCentre()
        right = pi2go.irRight()

        print
        ""
        print
        "Left:", left
        print
        "Center:", center
        print
        "Right:", right

        if not center and not left and not right:
            pi2go.go(91, 100)
        elif center and not left and not right:
            pi2go.spinLeft(100)
        elif center and left and not right:
            pi2go.spinRight(100)
            time.sleep(0.2)
        elif not center and left and right:
            pi2go.go(91, 100)
        elif not center and left and not right:
            pi2go.spinRight(100)
            time.sleep(0.2)
        elif not center and not left and right:
            pi2go.spinLeft(100)
        elif center and not left and right:
            pi2go.spinLeft(100)
            time.sleep(0.2)
        elif left and right and center:
            pi2go.reverse(60)
            time.sleep(0.2)
            pi2go.spinLeft(100)
            time.sleep(0.2)
            continue

        time.sleep(0.05)

except KeyboardInterrupt:
    print

finally:
    pi2go.cleanup()
