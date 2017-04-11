#!/usr/bin/env python
import OSC # https://github.com/ptone/pyosc
import pyautogui # http://pyautogui.readthedocs.io/en/latest/cheatsheet.html

server = OSC.OSCServer( ("localhost", 7110) )
server.timeout = 0
run = True

def messageHandler(path, tags, args, source):
    print path
    print tags

server.addMsgHandler( "/user/1", user_callback)
