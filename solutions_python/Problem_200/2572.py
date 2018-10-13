# -*- coding: UTF-8 -*-

""" Code template for Google Code Jam
    Eero Penttilä
    https://plus.google.com/111842998579946427698
"""

import os
import sys
import math
import copy

def prevNumber(n):
    if n == '0':
        return '9'
    else:
        return chr(ord(n)-1)

try:
    filename = sys.argv[1]
except Exception as inst:
    print ('Error: {0}\n\nPlease input the input file as parameter!\n\n'.format(inst))
else:
    filename = sys.argv[1]
    fin = open(filename, 'r')
    fout = open(filename[:-2]+'out', 'w')
    cases = int(fin.readline())
    print ('Cases {0}'.format(cases))

    for case in range(0, cases):
    #for case in range(0, 3):
        #print ("\nCase #{0}:".format(case+1))
        count = fin.readline().strip("\r").strip("\n")
        print ("\nInput#{0}: {1}".format(case+1, count))

        tidy = count
        curPos = 2
        curChar = count[-1]
        charToCorrect = 0

        while curPos <= len(count):
            #print (curPos, curChar, charToCorrect, tidy)
            if tidy[-curPos] > curChar:
                charToCorrect = curPos
                curChar = prevNumber(count[-curPos])
            else:
                curChar = count[-curPos]

            curPos += 1

        if charToCorrect:
            tidy = tidy[:-charToCorrect] + prevNumber(tidy[-charToCorrect]) + ('9' * (charToCorrect-1))
            if tidy[:1] == '0':
                tidy = tidy[1:]

        result = 'Case #{0}: {1}\n'.format(case+1, tidy)

        print (result)
        fout.write(result)
        
        
    fin.close()
    fout.close()
