def verticalline (x):  
    from gfxhat import lcd 
    lcd.clear()

    for i in range(64):
        lcd.set_pixel(x,i,1)
        lcd.show()

def horizontalline (y):
    from gfxhat import lcd
    lcd.clear()

    for i in range(128):
        lcd.set_pixel(i,y,1)
        lcd.show()
         
def staircase (x,y,width,height):
    from gfxhat import lcd
    lcd.clear()

    while x <128 and y <64:
        for i in range (height):
            lcd.set_pixel(x,y,1)
            lcd.show()
            y=y+1

        for i in range (width):
            lcd.set_pixel(x,y,1)
            lcd.show()
            x=x+1

def displayrandompixel(seconds):
    from gfxhat import lcd
    import random, time
    lcd.clear()

    x=random.rantint(1,128)
    y=random.randint(1,64)
    lcd.set_pixel(x,y,1)
    lcd.show()
    time.sleep(seconds)
    lcd.clear()

def clearbacklight():
    from gfxhat import backlight
    backlight.set_all(0,0,0)
    backlight.show()



        








