#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import time
'''Problem

Maria has been hired by the Ghastly Chemicals Junkies (GCJ) company to help them manufacture bullseyes. A bullseye consists of a number of concentric rings (rings that are centered at the same point), 
and it usually represents an archery target. GCJ is interested in manufacturing black-and-white bullseyes. 

 

Maria starts with t millilitres of black paint, which she will use to draw rings of thickness 1cm (one centimetre). A ring of thickness 1cm is the space between two concentric circles whose radii differ by 1cm.

Maria draws the first black ring around a white circle of radius r cm. Then she repeats the following process for as long as she has enough paint to do so:

Maria imagines a white ring of thickness 1cm around the last black ring.
Then she draws a new black ring of thickness 1cm around that white ring.
Note that each "white ring" is simply the space between two black rings.
The area of a disk with radius 1cm is π cm2. One millilitre of paint is required to cover area π cm2. What is the maximum number of black rings that Maria can draw? Please note that:
Maria only draws complete rings. If the remaining paint is not enough to draw a complete black ring, she stops painting immediately.
There will always be enough paint to draw at least one black ring.
Input

The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of a line containing two space separated integers: r and t.

Output

For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is the maximum number of black rings that Maria can draw.

'''
import math

def areaCirc(r):
    area =  r * r 
    return area

def analyse(r,t):
    maxrings = 0
    inkForRing = 0
    while t>=inkForRing:
        inkForRing = (areaCirc(r+1)-areaCirc(r))
        if inkForRing <= t:
            t -= inkForRing
            maxrings += 1
            r += 2
    return maxrings


start = time.time()
filein = open('A-small-attempt2.in.txt', 'r') 
#filein = open('Asample.in', 'r') 
outfile = open ('A.out', 'wt')
instances = int(filein.readline())

for i in range (instances):
    r,t = filein.readline().split()
    r = int(r)
    t = int(t)
    answer = analyse(r,t)
    print (r, ' ' ,t, ' ' , answer)
    stringStart = str('Case #' + str(i+1) + ': ')
    outfile.write(stringStart + str(answer))
    outfile.write('\n')
filein.close()
outfile.close()
print ('done in seconds -' , time.time() - start)