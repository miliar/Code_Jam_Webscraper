# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 20:41:45 2015

@author: Milos
"""


def procesTestCase(inputdata):
    smax, sequence = inputdata.split()       
    buff = 0
    retval = 0
    for x in xrange(0,int(smax)+1):
        if buff < x :
            buff = buff + 1
            retval = retval + 1
        buff = buff + int(sequence[x])
    return retval

infile = "A-large.in"
outfile = "output.txt"
with open(infile, "r") as inFile:
    with open(outfile,"w") as outFile:
        inFile.readline()
        x = 1
        for line in inFile:
            outFile.write("Case #" + str(x) + ": " + str(procesTestCase(line))+'\n')
            x = x+1
        