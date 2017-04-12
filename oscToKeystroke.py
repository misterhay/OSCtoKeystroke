#!/usr/bin/env python
import OSC # https://github.com/ptone/pyosc from https://trac.v2.nl/wiki/pyOSC
import pyautogui # http://pyautogui.readthedocs.io/en/latest/cheatsheet.html
import time
import threading

keyboardShortcuts = [ # can't include  *?,[]{}#
    'comma',
    'opensquare',
    'closesquare',
    'openparenthesis',
    'closeparenthesis',
    'pound',
    '"',
    "'",
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '0',
    '-',
    '=',
    '!',
    '@',
    'f1',
    'f2',
    'f3',
    'f4',
    'f5',
    'f6',
    'f7',
    'f8',
    'f9',
    'f10',
    'f11',
    'f12',
    '\\',
    'backspace',
    ';',
    '.',
    'space',
    'up',
    'down',
    'left',
    'right',
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z',
]

receiveAddress = ('0.0.0.0', 9000) # allow it to receive from any IP on port 9000
server = OSC.OSCServer(receiveAddress) # set up the OSC server

def messageHandler(path, tags, args, source):
    keystroke = path.lstrip('/')
    if keystroke == 'comma':
        keystroke = ','
    if keystroke == 'opensquare':
        keystroke = '['
    if keystroke == 'closesquare':
        keystroke = ']'
    if keystroke == 'openparenthesis':
        keystroke = '('
    if keystroke == 'closeparenthesis':
        keystroke = ')'
    if keystroke == 'pound':
        keystroke = '#'
    
    if args == [1.0]:
        pyautogui.typewrite(keystroke)
    if args == [2.0]: # shift
        pyautogui.hotkey('shift',keystroke)
    if args == [3.0]: # alt
        pyautogui.hotkey('alt',keystroke)
    if args == [4.0]: # ctrl
        pyautogui.hotkey('ctrl',keystroke)
        

for i in range(len(keyboardShortcuts)):
    server.addMsgHandler('/'+keyboardShortcuts[i], messageHandler)

threadingServer = threading.Thread(target = server.serve_forever)
threadingServer.start() # start the server thread we just defined
print 'OSC receiving server is running, press ctrl-c to quit'

try:
    while 1: # almost the same as while True:
        time.sleep(5) # do nothing here, just wait for ctrl-c

except KeyboardInterrupt: # what to do if there's a ctrl-c
    print 'Stopping the OSC receiving server...'
    server.close()
    threadingServer.join() # stop the thread
    print 'Server stopped'
