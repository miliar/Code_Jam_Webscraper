#!/usr/bin/env python
from __future__ import print_function, division

import sys
import math

infile = open(sys.argv[1])
outfiles = (sys.stdout, open(sys.argv[2], 'w'))

def read_in(infile):
    numLinesIsVariable=False # <<<<<< set this!
    numLinesInEntry=10 # <<<<<< set this!
    data = infile.readline()
    #print ('data0:',data)
    amount = int(data)
    content=[]
    for i in xrange(0,amount):
        if numLinesIsVariable:
            numLinesInEntry=int(infile.readline())
        for j in xrange(0,numLinesInEntry):
            content.append(infile.readline())

        #$print ('content1:',content)
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
    #print('===================do_task:' , content)
    ans1=int(content[0].strip())
    poss1=content[ans1].strip().split()
    ans2=int(content[5].strip())
    poss2=content[5+ans2].strip().split()

    #print('poss1:',poss1, 'poss2:',poss2)

    res=list(set(poss1).intersection(poss2))
    if len(res)==1:
        return res[0]
    elif len(res)==0:
        return  "Volunteer cheated!"
    else:
        return "Bad magician!"

main()
