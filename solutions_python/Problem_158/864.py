# -*- coding: UTF-8 -*-

""" Code template for Google Code Jam
    Eero Penttilä
    https://plus.google.com/111842998579946427698
"""

import os
import sys
import math
import copy


try:
    filename = sys.argv[1]
except Exception as inst:
    print ('Error: {0}\n\nPlease input the input file as parameter!\n\n'.format(inst))
else:
    filename = sys.argv[1]
    fin = open(filename, 'r')
    fout = open(filename[:filename.rfind('.')]+".out", 'w')
    cases = int(fin.readline())
    print ('Cases {0}'.format(cases))
    
    for case in xrange(0, cases):
    #for case in range(0, 3):
        print ("\nCase {0}".format(case+1))
        
        #people = int(fin.readline().strip("\r").strip("\n"))
        inut = map(int, fin.readline().strip("\r").strip("\n").split(" "))
        blocks = inut[0]
        area = inut[1:]
        area.sort()
        print blocks, area
        doable = False
        if (area[0] * area[1]) % blocks == 0:
            if blocks == 3 and area[0] == 1:
                doable = False
            elif blocks == 4 and (area[0] == 1 or area[0] == 2):
                doable = False
            else:
                doable = True

        if doable:
            result = 'Case #{0}: {1}\n'.format(case+1, 'GABRIEL')
        else:
            result = 'Case #{0}: {1}\n'.format(case+1, 'RICHARD')

        print (result)
        fout.write(result)
            
    fin.close()
    fout.close()
