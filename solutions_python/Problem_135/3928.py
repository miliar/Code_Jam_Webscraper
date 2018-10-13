#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      kirodh
#
# Created:     12/04/2014
# Copyright:   (c) kirodh 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from __future__ import print_function

from string import *

#a=[]
#b=[]

outfile = open('output.txt','w')
infile = open('A-small-attempt0.in','r')
for i in range(1,int(infile.readline())+1):
    tem = int(infile.readline())
    if tem == 1 :
        a= infile.readline().split(' ')
        infile.readline()
        infile.readline()
        infile.readline()
    elif tem ==2:
        infile.readline()
        a= infile.readline().split(' ')
        infile.readline()
        infile.readline()
    elif tem ==3:
        infile.readline()
        infile.readline()
        a= infile.readline().split(' ')
        infile.readline()
    elif tem ==4:
        infile.readline()
        infile.readline()
        infile.readline()
        a= infile.readline().split(' ')

    tem1 = int(infile.readline())

    if tem1 == 1 :
        b= infile.readline().split(' ')
        infile.readline()
        infile.readline()
        infile.readline()
    elif tem1 ==2:
        infile.readline()
        b= infile.readline().split(' ')
        infile.readline()
        infile.readline()
    elif tem1 ==3:
        infile.readline()
        infile.readline()
        b= infile.readline().split(' ')
        infile.readline()
    elif tem1 ==4:
        infile.readline()
        infile.readline()
        infile.readline()
        b= infile.readline().split(' ')
    for k in range(4):
        hold=int(a[k])
        a[k] = hold
        hold1=int(b[k])
        b[k] = hold1

    array=[]
    for l in a:
        for m in b:
            if l == m:
                #print(l,m)
                array.append(l)
    if len(array) > 1:
        print('Case #',i,': ','Bad magician!',sep='',file=outfile)
    elif len(array) == 1:
        print('Case #',i,': ',array[0] ,sep='',file=outfile)
    else:
        print('Case #',i,': ','Volunteer cheated!',sep='',file=outfile)
    #print(array)
    #print(len(array))
    #print(a,b)
    del array
outfile.close()
infile.close()