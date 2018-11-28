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

    for case in xrange(0, cases):
    #for case in range(0, 3):
        print ("\nCase {0}".format(case+1))
        shyness, people = fin.readline().strip("\r").strip("\n").split(" ")
        shyness = int(shyness)
        #print (shyness, people)
        total_people = 0
        max_needed = 0
        for lev in xrange(1, shyness+2):
            
            total_people += int(people[0])
            if total_people + max_needed < lev:
                max_needed += 1

            #print lev-1, int(people[0]), max_needed
            people = people[1:]

        result = 'Case #{0}: {1}\n'.format(case+1, max_needed)

        print (result)
        fout.write(result)
        
        
    fin.close()
    fout.close()
