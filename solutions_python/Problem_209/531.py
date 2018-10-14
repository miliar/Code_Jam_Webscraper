# -*- coding: UTF-8 -*-

""" Code template for Google Code Jam
    Eero Penttilä
    https://plus.google.com/111842998579946427698
"""

import os
import sys
import math
import copy
from operator import itemgetter

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
        rows, order = map(int, fin.readline().strip("\r").strip("\n").split(" "))
        print ("\nCase #{0}: {1}/{2}".format(case+1, rows, order))

        #print (rows, order)

        cakes = []
        for i in range(0,rows):
            radius, height = map(int, fin.readline().strip("\r").strip("\n").split(" "))
            cakes.append([radius**2, 2*radius*height])


        cakes.sort(key=itemgetter(1), reverse=True)
        '''
        for line in cakes:
            print (line, line[0]+line[1])

        #proof of consept, with 2 cakes served
        top = []
        maxTotal = 0
        for x in range(0, len(cakes)):
            for y in range(0, len(cakes)):
                if x != y:
                    total =  cakes[x][0] + cakes[x][1] + cakes[y][1]
                    if total > maxTotal:
                        maxTotal = total
                        top = [x,y]

        print (maxTotal, top)
        '''

        #Brute force approach, try all combinations
        maxTotal = 0
        for i in range(0, len(cakes)):
            total = cakes[i][0] + cakes[i][1]
            if i < order:
                #if line in range of order, exclude it
                for a in range(0, order):
                    if a != i:
                        total += cakes[a][1]
            else:
                #line not in range
                for a in range(0, order-1):
                    total += cakes[a][1]
            if total > maxTotal:
                maxTotal = total
        #print (maxTotal)


        result = 'Case #{0}: {1}\n'.format(case+1, maxTotal*math.pi)

        print (result)
        fout.write(result)
        

        
        
    fin.close()
    fout.close()
