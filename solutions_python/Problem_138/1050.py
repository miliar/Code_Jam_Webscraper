#!/usr/bin/env python
from __future__ import print_function, division

import sys
import math

infile = open(sys.argv[1])
outfiles = (sys.stdout, open(sys.argv[2], 'w'))

def read_in(infile):
    numLinesIsVariable=False # <<<<<< set this!
    numLinesInEntry=3 # <<<<<< set this!
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
    #print('===================do_task:')
    num=int(content[0].strip())
    naomi=[float(i) for i in content[1].strip().split()]
    ken=[float(i) for i in content[2].strip().split()]
    #print('naomi:' , naomi)
    #print('ken:' , ken)
    
    naomi.sort()
    ken.sort()
    
    #print('naomi:' , naomi)
    #print('ken:' , ken)
    res1=0
    res2=0

    #deceit
    arr1=naomi[::-1]
    arr2=ken[::-1]
    while len(arr1)>0:
        if arr1[0]>arr2[0]:
            res1+=1
            arr1.remove(arr1[0])
            arr2.remove(arr2[0])
        else:
            arr1.remove(arr1[-1])
            arr2.remove(arr2[0])


    #war
    arr1=list(naomi)
    arr2=list(ken)
    i=0
    j=0
    #print('arr1',arr1)
    for i in xrange(0,num):
        foundNum=None
        for j in xrange(0,len(arr2)):
            #print('arr2',len(arr2),i,j, arr2)
            if arr2[j]>arr1[i]: 
                foundNum=arr2[j]
                #print('found',foundNum)
                break

        if foundNum!=None:
            arr2.remove(foundNum)
            #print(arr1[i],'removed',foundNum)
        else: 
            toRemove=arr2[0]
            arr2.remove(toRemove)
            #print(arr1[i],'removed smaller',toRemove)
            res2+=1

    return str(res1)+' '+str(res2)

main()
