import time, ttspi2go

ttspi2go.init()

speed = 100
rspeed = 100
sspeed = 100

try:
    while True:
        time.sleep(0.1)
        ttspi2go.forward(speed)
        if ttspi2go.irCentre() == True:
            print("Front sensors triggered, reversing right.")
            ttspi2go.reverse(speed)
            time.sleep(0.3)
            ttspi2go.spinRight(sspeed)
            time.sleep(0.3)
            ttspi2go.stop()

        elif ttspi2go.irLeft() == True and ttspi2go.irCentre() == True:
            print("Front & Left Sensors triggered, turning right.")
            ttspi2go.spinRight(sspeed)
            time.sleep(0.3)
            ttspi2go.stop()

        elif ttspi2go.irLeft() == True:
            print("Left Sensors triggered, turning right.")
            ttspi2go.spinRight(sspeed)
            time.sleep(0.3)
            ttspi2go.stop()


        elif ttspi2go.irRight() == True and ttspi2go.irCentre() == True:
            print("Front & Right Sensors triggered, turning left.")
            ttspi2go.spinLeft(sspeed)
            time.sleep(0.3)
            ttspi2go.stop()

        elif ttspi2go.irRight() == True:
            print("Right Sensors triggered, turning left.")
            ttspi2go.spinLeft(sspeed)
            time.sleep(0.3)
            ttspi2go.stop()


except KeyboardInterrupt:
    print("Sutting Down")

finally:
    ttspi2go.cleanup()

