#!/usr/bin/env python
# encoding: utf-8
"""
reverse_words.py

Created by Joshua Olson on 2011-05-05.
Copyright (c) 2011 solarmist. All rights reserved.
"""

import sys
import os


def main():
    data = sys.stdin.readlines()
    for line in range(int(data[0])): #line is an int containing the index of the case
        print 'Case #' + str(line + 1) + ':',
        case = data[line + 1].split()
        buttons = int(case.pop(0))
        totalTime = 0
        O = 1 #starting positions
        B = 1
        #output is the max of the time for each button
        bufferO = 0
        bufferB = 0
        
        for n in range(buttons):
            bot = case.pop(0) 
            button = int(case.pop(0))
            buffer = 0
            botPos = 0
            moveTime = 0
            if bot == 'O':
                botPos = O
                buffer = bufferO
                bufferO = 0
            else:
                botPos = B
                buffer = bufferB
                bufferB = 0
            moveTime = 1 + max(0, abs(button - botPos) - buffer) #1 to push the button + time to move from the button we were at - the buffer time
            botPos = button #We've moved to the new button
            #update the current position
            if bot == 'O':
                O = botPos
                bufferB += moveTime
            else:
                B = botPos
                bufferO += moveTime
            
            totalTime += moveTime
        print totalTime


if __name__ == '__main__':
	main()

