def servoAdjust():
    global servoNum, adjNum, runservo
    servoNum = 0
    adjNum = 0
    while loop:
        if input.button_is_pressed(Button.AB):
            adjNum = runservo
            basic.show_number(adjNum)
        elif input.button_is_pressed(Button.A):
            servoNum += 1
            runservo = servoNum
            basic.show_number(runservo)
        elif input.button_is_pressed(Button.B):
            servoNum += -1
            runservo = servoNum
            basic.show_number(runservo)
        elif servoNum > 4:
            basic.show_icon(IconNames.SAD)
            basic.show_number(servoNum)
        if adjNum == 1:
            basic.show_number(servoNum)
            kitronik_i2c_16_servo.servo_write(kitronik_i2c_16_servo.Servos.SERVO1, 89)
            basic.pause(100)
            kitronik_i2c_16_servo.servo_write(kitronik_i2c_16_servo.Servos.SERVO1, 4)
            basic.show_leds("""
                # # . # #
                                # # # # #
                                # # # # #
                                . . # # #
                                . . # # #
            """)
            basic.pause(50)
        elif adjNum == 2:
            basic.show_number(servoNum)
            kitronik_i2c_16_servo.servo_write(kitronik_i2c_16_servo.Servos.SERVO2, 57)
            basic.pause(100)
            kitronik_i2c_16_servo.servo_write(kitronik_i2c_16_servo.Servos.SERVO2, 0)
            basic.show_leds("""
                # # . # #
                                # # # # #
                                # # # # #
                                # # # . .
                                # # # . .
            """)
        elif adjNum == 3:
            basic.show_number(servoNum)
            kitronik_i2c_16_servo.servo_write(kitronik_i2c_16_servo.Servos.SERVO3, 138)
            basic.pause(100)
            kitronik_i2c_16_servo.servo_write(kitronik_i2c_16_servo.Servos.SERVO3, 0)
            basic.show_leds("""
                # # # # .
                                # # # # .
                                . . # # .
                                . . # # .
                                . . # # .
            """)
        elif adjNum == 4:
            basic.show_number(servoNum)
            kitronik_i2c_16_servo.servo_write(kitronik_i2c_16_servo.Servos.SERVO5, 61)
            basic.pause(100)
            kitronik_i2c_16_servo.servo_write(kitronik_i2c_16_servo.Servos.SERVO5, 128)
            basic.show_leds("""
                . # # # #
                                . # # # #
                                . # # . .
                                . # # . .
                                . # # . .
            """)
runservo = 0
adjNum = 0
servoNum = 0
loop = False
basic.show_icon(IconNames.HAPPY)
loop = True

def on_forever():
    servoAdjust()
basic.forever(on_forever)
