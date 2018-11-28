#!/usr/bin/env python

import numpy as np
import sys
# import os

def popcharacter(s, c):
    new=[]
    pop=1
    for sc in s:
        if (sc==c):
            if(pop==1):
                pop=0
            else:
                new.append(sc)
        else:
            new.append(sc)
    new = ''.join(new)
    return new

def popdigit(s, sdigit, feature):
    current = s
    count = 0
    while feature in current:
        count += 1
        for sc in sdigit:
            tmp = popcharacter(current, sc)
            current = tmp
            # print current
    return count, current



def getDigits(s):
    seq = np.array([('0', 0), ('1', 0), ('2', 0), ('3', 0), ('4', 0), ('5', 0), ('6', 0), ('7', 0), ('8', 0), ('9', 0)], dtype=[('digit', 'S1'), ('num', 'i1')])
    current = s
    seq['num'][0] , current = popdigit(current, 'ZERO', 'Z')
    seq['num'][2] , current = popdigit(current, 'TWO', 'W')
    seq['num'][4] , current = popdigit(current, 'FOUR', 'U')
    seq['num'][6], current = popdigit(current, 'SIX', 'X')

    seq['num'][1], current = popdigit(current, 'ONE', 'O')
    seq['num'][3], current = popdigit(current, 'THREE', 'R')
    seq['num'][5], current = popdigit(current, 'FIVE', 'F')
    seq['num'][7], current = popdigit(current, 'SEVEN', 'V')
    seq['num'][8], current = popdigit(current, 'EIGHT', 'G')
    seq['num'][9], current = popdigit(current, 'NINE', 'N')

    # print seq

    phonenumber = []
    for c in seq:
        # print c['digit'] * c['num']
        phonenumber.append( str(c['digit'] ) * int( c['num']))
    phonenumber = ''.join(phonenumber).strip()
    return phonenumber




filename = sys.argv[1]
f = open(filename)
nround = np.int(f.readline())
iround = 0

for line in f.readlines():
    iround += 1
    # print line
    phonenumber = getDigits(str(line))
    print "Case #{0}: {1}".format(iround, phonenumber)
