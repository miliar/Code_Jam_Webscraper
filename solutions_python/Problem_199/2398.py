# -*- coding: UTF-8 -*-

""" Code template for Google Code Jam
    Eero Penttilä
    https://plus.google.com/111842998579946427698
"""

import os
import sys
import math
import copy

def flip(c, w, pos):
    f = ""
    for i in range(pos, pos+w):
        if c[i] == '-':
            f += '+'
        else:
            f += '-'
    return c[:pos] + f + c[pos+w:]


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
        print ("\nCase #{0}:".format(case+1))
        cakes, width = fin.readline().strip("\r").strip("\n").split(" ")
        width = int(width)
        numCakes = len(cakes)
        print (cakes, width, numCakes)

        pos = cakes.find('-')
        err = False
        flips = 0

        while pos != -1 and not err:
            #print (cakes, pos, width, flips)
            if pos + width <= numCakes:
                cakes = flip(cakes, width, pos)
                flips += 1
            else:
                err = True
            pos = cakes.find('-')
 
        print (cakes, width)

        if not err:
            result = 'Case #{0}: {1}\n'.format(case+1, flips)
        else:
            result = 'Case #{0}: {1}\n'.format(case+1, "IMPOSSIBLE")

        print (result)
        fout.write(result)

        
        
    fin.close()
    fout.close()
