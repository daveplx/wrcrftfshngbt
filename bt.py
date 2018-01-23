# Import Modules

import os
import ctypes
import autopy

# Initialize variables

dev = True

screenSize = None

# Define methods

def isProcessRunning(processName):
    processIsRunning = False
    parameterString = 'tasklist /v /FO LIST /FI "IMAGENAME eq "' + processName + '"'
    processStatus = os.popen(parameterString).read().strip().split('\n')
    for attribute in processStatus:
        if 'Status' in attribute:
            if 'Running' in attribute:
                processIsRunning = True
    return processIsRunning


def getProcessIdByName(processName):
    parameterString = 'tasklist /FO LIST /FI "STATUS eq RUNNING" /FI "IMAGENAME eq "' + processName + '"'
    processId = os.popen(parameterString).read().strip().split('\n')[1][4:].strip()
    return processId

def setScreenSize():
    global screenSize
    user32 = ctypes.windll.user32
    screenSize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

def getScreenSize():
    global screenSize
    return screenSize

def character_jump():
    pass

def character_cast_rod():
    pass

def character_find_bobber():
    pass

def move_mouse():
    pass

def listen_for_sound():
    pass

def character_reel_bobber():
    pass

if __name__ == "__main__":

    # Check if our process is running
    processName = 'Explorer.exe'
    processRunning = isProcessRunning(processName)
    if not processRunning:
        if dev: print('Process ' + processName + ' is not running.')
        exit(1)
    else:
        if dev: print('Process ' + processName + ' is running.')

    setScreenSize()

    print(getScreenSize())