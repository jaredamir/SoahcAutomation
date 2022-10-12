import pyautogui
import time


print("Open Soahc in Full Screen Mode, Click Enable Content Before Entering Information, Open Blood Chart and Minimize Tab, then Open Consent Tab Before Continuing")
print('Make Sure to Have App Order: [File Explorer, Explorer, Soahc (Only Soahc), Chrome]')
print('On Taskbar; Have SPPB CSV Window on the right and SAVE DATA HERE Window on the left; Do Not Change Window Size of Chrome; Add W_MRN Filter Before Starting')
print('If W_Final Click Is Not Working, Make The Right Side of Chrome Window Smaller Very Very Slightly')
pyautogui.FAILSAFE = True
try:
    nFileExplorerCoords = 466, 877 #input('Coordinates of "File Explorer" taskbar window: ')
    nSaveDataCoords = input('Coordinates of "SAVE DATA HERE" taskbar window: ')
    nSppbCvsFilesCoords = input('Coordinates of "SPPB CSV Files" taskbar window: ')
    nCoords = input('Cordinates for SPPB CSV File Window Search Bar X, Y: ')
    vDate = raw_input('Vist Date for This Folder (Restart After Finishing Folder): ')
    while True:
        #Initial Search
        #Inputs
        wNum = raw_input('W#: ')
        vNum = raw_input('Vist#: ')
        nBlooderror1 = raw_input('Is There Blood Data Report? (Y or N): ')
        nSRerror1 = raw_input('Is There a SR Reported? (Y or N): ')
        pMOCA = raw_input('Is There a MOCA paper Copy? (Y or N): ')
        nSPPBerror1 = raw_input('Is There an SPPB Reported? (Y or N): ')

        raw_input('Have One Window Open Besides Soahc then Press Enter to Continue ')
        # Soahc Click to Minimize Windows
        pyautogui.click(566, 880)
        time.sleep(.1)

        #Chrome Click
        pyautogui.click(610, 880)
        time.sleep(.1)

        # Filter
        pyautogui.click(220, 265)
        time.sleep(.1)
        pyautogui.click(590, 275)
        time.sleep(.1)
        # Is
        pyautogui.click(500, 265)
        time.sleep(.1)
        pyautogui.click(550, 300)
        time.sleep(.1)
        # WNumber
        pyautogui.click(570, 265)
        time.sleep(.1)
        for i in range(0, 15):
            pyautogui.hotkey('backspace')
        pyautogui.typewrite(wNum + '\n')
        time.sleep(.1)

        for i in range(0, 15):
            pyautogui.hotkey('backspace')
        pyautogui.typewrite(wNum + '\n')
        time.sleep(.1)

        # Is Fail check
        pyautogui.click(500, 265)
        time.sleep(.1)
        pyautogui.click(550, 337)
        time.sleep(.1)
        pyautogui.click(500, 265)
        time.sleep(.1)
        pyautogui.click(550, 300)
        time.sleep(.1)

        #raw_input('Press Any Key to Check Final: ')
        nFinal = raw_input('Check Final? (Y/N): ')
        if nFinal.strip().capitalize() == 'Y':
            # Wfinal
            pyautogui.click(220, 265)
            time.sleep(1)
            pyautogui.moveTo(600, 230, .2)
            pyautogui.moveTo(390, 230, .2)
            pyautogui.moveTo(330, 660, .2)
            pyautogui.click(330, 660)
            time.sleep(.3)
            # Is p.2
            pyautogui.click(350, 265)
            time.sleep(.3)
            pyautogui.click(330, 300)
            time.sleep(.5)
            # WNum to Close Warning Click
            pyautogui.click(380, 265)
            time.sleep(3)
            pyautogui.click(750, 620)
            time.sleep(.3)
            pyautogui.click(380, 265)
            time.sleep(.1)
            for i in range(0, 15):
                pyautogui.hotkey('backspace')
            pyautogui.typewrite(wNum + '\n')
            time.sleep(.5)
            pyautogui.click(550, 200)
            time.sleep(2)

#MIGHT  BE AN ERROR HERE****
        sReport = raw_input('Is There a Self Report In Qualtrics? (Y or N): ')
        # Close Tab Click
        pyautogui.click(935, 25)
        time.sleep(.1)
        #Initial scroll Reset
        pyautogui.click(1426, 215)
        time.sleep(0.01)
        pyautogui.click(1426, 215)
        time.sleep(0.01)
        #Enter W#
        pyautogui.click(232, 564)
        time.sleep(0.01)
        pyautogui.click(232, 564)
        time.sleep(0.01)
        for i in range(0, 15):
            pyautogui.hotkey('backspace')
        pyautogui.typewrite(wNum + '\n')

        #Scroll
        pyautogui.moveTo(1430, 280)
        pyautogui.dragTo(1430, 280+280, duration=1.0)
        pyautogui.moveTo(1430, 280+280)
        pyautogui.dragTo(1430, 280, duration=0.5)
        #SR Tab CLick
        pyautogui.click(100, 600)
        time.sleep(0.01)

        #____________________________________________



        # Add Record
        pyautogui.click(660, 430)
        time.sleep(0.01)

        #SR visit number
        pyautogui.click(184, 430)
        time.sleep(0.01)
        pyautogui.click(184, 430)
        time.sleep(0.01)
        pyautogui.typewrite(vNum)

        #SR visit date
        pyautogui.click(170, 460)
        time.sleep(0.01)
        pyautogui.click(170, 460)
        time.sleep(0.01)
        pyautogui.typewrite(vDate)

        #Completion Conditions
        if sReport.strip().capitalize() == 'Y': #yes condition
            #Paper or Electronic Dropdown Menu Click
            pyautogui.click(266, 500)
            time.sleep(0.01)
            #Electronic at clinic Click
            pyautogui.click(222, 537)
            time.sleep(0.01)
            pyautogui.click(222, 537)
            time.sleep(0.01)
            #Status Drop Down Menu Click
            pyautogui.click(266, 528)
            time.sleep(0.01)
            #Status Complete Click
            pyautogui.click(220, 550)
            time.sleep(0.01)
            #Data Entry Status Drop Down Menu Click
            pyautogui.click(265, 560)
            time.sleep(0.01)
            #Data Entry Status NA Click
            pyautogui.click(220, 620)
            time.sleep(0.01)
        else: #no condition
            # Paper or Electronic Dropdown Menu Click
            pyautogui.click(266, 500)
            time.sleep(0.01)
            # Not Completed Click
            pyautogui.click(220, 553)
            time.sleep(0.01)
            # Status Drop Down Menu Click
            pyautogui.click(266, 528)
            time.sleep(0.01)
            # Status Patient Missed Click
            pyautogui.click(220, 606)
            time.sleep(0.01)
            # Data Entry Status Drop Down Menu Click
            pyautogui.click(265, 560)
            time.sleep(0.01)
            # Data Entry Status NA Click
            pyautogui.click(220, 620)
            time.sleep(0.01)

        #_______________

        #MOCA Tab CLick
        pyautogui.click(150, 282)
        time.sleep(0.01)

        #Moca Checkbox Click Conditions
        if pMOCA.strip().capitalize() == 'Y':
            pyautogui.click(200, 520)
            time.sleep(0.01)
            # Blood Tab Click
            pyautogui.click(280, 280)
            time.sleep(0.01)
        else:
            #Blood Tab Click
            pyautogui.click(280, 280)
            time.sleep(0.01)


        #_____________________________________________
        #Blood List tab Click
        pyautogui.click(82, 842)
        time.sleep(0.01)

        #print('Please Check Blood Data Then Minimize Tab Before Entering Information')

        #Table CLicks
        nBlue = raw_input('Blue Marble #: ')
        nPurple = raw_input('Purple #: ')
        nOM = raw_input('Orange Marble #: ')
        nOrange = raw_input('Orange #: ')
        #Blood Data window close
        pyautogui.click(1322, 11)
        time.sleep(0.01)

        # Add Record
        pyautogui.click(400, 420)
        time.sleep(0.01)

        #Visit Type Drop Down Menu Click
        pyautogui.click(250, 420)
        time.sleep(0.01)

        #Montioring Click
        pyautogui.click(220, 560)
        time.sleep(0.01)

        #MOCA Vist Number CLick
        pyautogui.click(220, 460)
        time.sleep(0.01)
        pyautogui.typewrite(vNum)

        #MOCA Visit Date Click
        pyautogui.click(220, 490)
        time.sleep(0.01)
        pyautogui.typewrite(vDate)



        #Blue Marble Click
        if int(nBlue) > 0: #GEEK OUT TO KEVIN
        #Blue Marble Number Click
            pyautogui.click(444, 575)
            time.sleep(0.01)
            pyautogui.hotkey('backspace')
            pyautogui.typewrite(nBlue)
        #Blue Marble Drop Down Menu Click
            pyautogui.click(290, 580)
            time.sleep(0.01)
        #Blue Marble YES Click
            pyautogui.click(290, 600)
            time.sleep(0.01)
        else:
            # Blue Marble Drop Down Menu Click
            pyautogui.click(290, 580)
            time.sleep(0.01)
            # Blue Marble NO Click
            pyautogui.click(290, 620)
            time.sleep(0.01)


        #Purple Clicks
        if int(nPurple) > 0: #GEEK OUT TO KEVIN
        #Purple Number Click
            pyautogui.click(444, 610)
            time.sleep(0.01)
            pyautogui.hotkey('backspace')
            pyautogui.typewrite(nPurple)
        #Purple Drop Down Menu Click
            pyautogui.click(290, 610)
            time.sleep(0.01)
        #Purple YES Click
            pyautogui.click(290, 635)
            time.sleep(0.01)
        else:
            # Purple Drop Down Menu Click
            pyautogui.click(290, 610)
            time.sleep(0.01)
            # Purple NO Click
            pyautogui.click(290, 655)
            time.sleep(0.01)


        #Orange Marble
        if int(nOM) > 0: #GEEK OUT TO KEVIN
        #Orange Marble Click
            pyautogui.click(444, 640)
            time.sleep(0.01)
            pyautogui.hotkey('backspace')
            pyautogui.typewrite(nOM)
        #Orange Marble Drop Down Menu Click
            pyautogui.click(290, 640)
            time.sleep(0.01)
        #Orange Marble YES Click
            pyautogui.click(290, 665)
            time.sleep(0.01)
        else:
            # Orange Marble Drop Down Menu Click
            pyautogui.click(290, 645)
            time.sleep(0.01)
            # Orange Marble NO Click
            pyautogui.click(290, 685)
            time.sleep(0.01)


        #Orange Clicks
        if int(nOrange) > 0: #GEEK OUT TO KEVIN
        #Orange Click
            pyautogui.click(444, 675)
            time.sleep(0.01)
            pyautogui.hotkey('backspace')
            pyautogui.typewrite(nOrange)
        #Orange Drop Down Menu Click
            pyautogui.click(290, 675)
            time.sleep(0.01)
        #Orange Marble YES Click
            pyautogui.click(290, 695)
            time.sleep(0.01)
        else:
            # Orange Drop Down Menu Click
            pyautogui.click(290, 675)
            time.sleep(0.01)
            # Orange NO Click
            pyautogui.click(290, 715)
            time.sleep(0.01)

        #Yello Clicks
        # Yellow Drop Down Menu Click
        pyautogui.click(290, 700)
        time.sleep(0.01)
        # Yellow NO Click
        pyautogui.click(290, 745)
        time.sleep(0.01)

        #SPPB Tab Click
        pyautogui.click(330, 280)
        time.sleep(0.01)

        #___________________________________________
        # SPPB Folder Window Opener

        # File Explorer Click
        pyautogui.click(nFileExplorerCoords)  # 466, 866
        time.sleep(.01)
        # SAVE DATA HERE Click
        pyautogui.click(nSppbCvsFilesCoords)  # 644, 789
        time.sleep(1)
        # File Explorer Click P.2
        pyautogui.click(nFileExplorerCoords)
        time.sleep(.01)
        # SPPB CSV Files Click
        pyautogui.click(nSaveDataCoords)  # 252, 789
        time.sleep(.1)

        pyautogui.click(nCoords)  # ****ADD CONFIRMATION IF THEN**
        time.sleep(.5)
        pyautogui.hotkey('end')
        for i in range(0, 15):
            pyautogui.hotkey('backspace')
        pyautogui.typewrite(wNum + "\n")
        time.sleep(.1)

        nCVS = raw_input('Is There an CVS File in the Drive? (Y or N): ')

        if nCVS.strip().capitalize() == 'Y':
            # File Mover
            pyautogui.click(nCoords[0], nCoords[1] + 55)
            pyautogui.moveTo(nCoords[0] - 500, nCoords[1] + 55)
            pyautogui.dragTo(nCoords[0] + 700, nCoords[1] + 200, duration=1.0)
            # 833, 184
            # Qualtrics Cilck
            pyautogui.click(400, 10)
            time.sleep(0.01)

            # CVS File Drop Down Menu CLick
            pyautogui.click(260, 560)
            time.sleep(0.01)
            # CVS File YES Click
            pyautogui.click(260, 580)
            time.sleep(0.01)

            pyautogui.click(42, 278)
            time.sleep(0.01)


        else:
            # Qualtrics Cilck
            pyautogui.click(400, 10)
            time.sleep(0.01)
            # CVS File Drop Down Menu CLick
            pyautogui.click(260, 560)
            time.sleep(0.01)
            # CVS File No Click
            pyautogui.click(260, 600)
            time.sleep(0.01)
            pyautogui.click(800, 26)
            time.sleep(1)
            pyautogui.click(42, 278)
            time.sleep(0.01)
        #Error Report
        print('Error Report')

        if nSPPBerror1.strip().capitalize() == 'Y' and nCVS.strip().capitalize() != 'Y':
            print(wNum + ' Has no CSV File ')

        if nSPPBerror1.strip().capitalize() != 'Y' and nCVS.strip().capitalize() == 'Y':
            print(wNum + ' Has CSV File but Reported as Not in Summary ')

        #Blood Error Conditions
        if nBlooderror1.strip().capitalize() == 'Y' and int(nBlue) == 0 and int(nPurple) == 0 and int(nOM) == 0 and int(
                nOrange) == 0:
            print(wNum + ' Has No Blood Data')

        if nBlooderror1.strip().capitalize() != 'Y' and (
                int(nBlue) > 0 or int(nPurple) > 0 or int(nOM) > 0 or int(nOrange) > 0):
            print(wNum + ' Has Blood Data but Reported as Not in Summary')

        #SR Error Conditions
        if nSRerror1.strip().capitalize() == 'Y' and sReport.strip().capitalize() != 'Y':
            print(wNum + ' Has No SR in Qualtrics')

        if nSRerror1.strip().capitalize() != 'Y' and sReport.strip().capitalize() == 'Y':
            print(wNum + ' Has SR in Qualtrics but Reported as Not in Summary')

        raw_input('Press Enter After Writing Error Report to Continue')
except KeyboardInterrupt:
    print(" Quitting")



