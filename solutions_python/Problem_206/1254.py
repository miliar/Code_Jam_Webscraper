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
    fout = open(filename[:-2]+'out', 'w')
    cases = int(fin.readline())
    print ('Cases {0}'.format(cases))

    for case in range(0, cases):
    #for case in range(0, 3):
        #print ("\nCase #{0}:".format(case+1))
        destination, horse = map(int, fin.readline().strip("\r").strip("\n").split(' '))
        print ("\nInput#{0}: {1} {2}".format(case+1, destination, horse))

        horses = []

        for r in range(0,horse):
            k, s =  fin.readline().strip("\r").strip("\n").split(' ')
            horses.append([int(k), int(s)])

        print (horses)

        slower = 0

        for h in horses:
            time = (destination-h[0])/h[1]
            if time > slower:
                slower = time

        #print (time, destination/slower)

        result = 'Case #{0}: {1}\n'.format(case+1, destination/slower)

        print (result)
        fout.write(result)

        
        
    fin.close()
    fout.close()
