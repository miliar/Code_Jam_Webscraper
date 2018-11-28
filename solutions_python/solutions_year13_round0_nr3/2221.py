#!/usr/bin/env python
from __future__ import print_function, division

import sys
import math

infile = open(sys.argv[1])
outfiles = (sys.stdout, open(sys.argv[2], 'w'))

def read_in(infile):
    numLinesIsVariable=False # <<<<<< set this!
    numLinesInEntry=1 # <<<<<< set this!
    data = infile.readline()
    #print ('data0:',data)
    amount = int(data)
    content=[]
    for i in xrange(0,amount):
        if numLinesIsVariable:
            numLinesInEntry=int(infile.readline().split()[0])
        for j in xrange(0,numLinesInEntry):
            content.append(infile.readline())
        yield content
        content=[]

def do_output(number, output, outfiles):
    for f in outfiles:
        print('Case #%d:' % number, output, file=f)

def main():
    for i, content in enumerate(read_in(infile)):
        do_output(i+1, do_task(content), outfiles)

def do_task(content):
    # Parse input string
    content=content[0].strip()
    #print('content:',content)
    content=content.split()
    start,end=int(content[0]),int(content[1])
    #print('start',start,'end',end)
    ctr=0
    for i in xrange(start,end+1):
        #print('i',i)
        #iRev=`i`
        #iRev.reverse()
        iSqrtInt=int(math.sqrt(i))
        #print('test1',iRev,i)
        #print('test2',math.sqrt(i),iSqrtInt)
        if `i`==`i`[::-1] and math.sqrt(i)==iSqrtInt and `iSqrtInt`==`iSqrtInt`[::-1]:
            #print('ans i:', i)
            ctr+=1
    return ctr

main()
