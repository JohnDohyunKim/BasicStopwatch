#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 16:01:49 2022

Stopwatch

@author: johnkim
"""

import time 

def stopwatch():
    """
    a watch that starts and stops according to user input
    """
    start_timer = input("To start, type: y \n")
    button1 = start_timer.lower().replace(" ", "")
    if (button1 == "y"):
        #start timer
        start_time = time.time()
        paused_time = 0
        resumed_time = 0
        pause = input("To pause, type: p \n")
        if (pause.lower().replace(" ", '') == "p"):
            #pause the timer
            paused_time = time.time()
            resume = input("To resume, type: r \n")
            if (resume.lower().replace(" ", "") == "r"):
                #resume the timer
                resumed_time = time.time()
        end = input("To end, type: y \n")
        button2 = end.lower().replace(" ", "")
        if (button2 == "y"):
            #stop timer
            return print("Time Passed:", round(time.time() - start_time - (resumed_time-paused_time), 2))
            start_time = 0
    else:
        return print("Program End")
    
    