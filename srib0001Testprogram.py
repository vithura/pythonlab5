userchoice = 0
print ("Hello testprogram")

print ("enter 1 for display vertical line")
print ("enter 2 for display horizontal line")
print ("enter 3 for display stiarcase ")
print ("enter 4 for display randompixel")
print ("enter 5 for  display clear backlight")
print ("enter 6 to quit")

while userchoice !=6:
    userchoicestring = input("make a choice")
    userchoice=int(userchoicestring)

    if userchoice ==1:
        from srib0001Gfxlibrary import verticalline
        verticalline(30)

    elif userchoice ==2:
         from srib0001Gfxlibrary import horizontalline
         horizontalline(35)

    elif userchoice ==3:
        from srib0001Gfxlibrary import staircase
        staircase(25,20,15,5)

    elif userchoice ==4:
        from srib0001Gfxlibrary import displayrandompixel
        displayrandompixel(3)

    elif userchoice ==5:
        from srib0001Gfxlibrary import clearbacklight
        clearbacklight()

    else :
        print ("try again")

    





