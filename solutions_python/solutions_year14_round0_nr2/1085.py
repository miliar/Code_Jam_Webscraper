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
    c=(content[0].strip().split())
    #print('c0',c[0])
    C,F,X=float(c[0]), float(c[1]),float(c[2])
    totalTime=0
    nowSum=0
    nowRate=2

    while nowSum<X:
        #print ('time now :',totalTime, 'rate now',nowRate)

        time2x=X/nowRate
        time2fac=(C/nowRate)
        #time2xbuy=time2fac + (X+C)/(nowRate+F)
        time2xbuy=time2fac + (X)/(nowRate+F)

        #print ('time2x:',time2x,'time2xbuy',time2xbuy, 'time2fac',time2fac)
        if time2xbuy>time2x:
            totalTime+=time2x
            break
            #nowSum+=(time2x * nowRate)

        else: #buy new factory
            totalTime+=time2fac
            nowSum=0

            nowRate+=F
            #print('buy new fac')
            
    #print ('time now :',totalTime, 'rate now',nowRate)

    return '%.7f' % totalTime

main()
