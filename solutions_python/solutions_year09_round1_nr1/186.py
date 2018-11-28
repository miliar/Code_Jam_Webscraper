#!/usr/bin/python
'''
Solution for Google Code Jam
Created on 2009-9-11
@author: Qihe Bian
'''
import sys
import re
from collections import *

class Buffer:
    buffer=''
    def write(self, s):
        Buffer.buffer += s
    def __str__(self):
        return Buffer.buffer
    def __repr__(self):
        return Buffer.buffer
    
def getdigit(num,base):
    a=[]
    while num>0:
        a+=[num%base]
        num/=base
    return a

def ishappy(num,base,level):
    if num==1:
        return True
    if level>base*(base-1):
        return False
    a=getdigit(num, base)
    num=0
    for i in range(len(a)):
        num+=a[i]*a[i]
    if num<base*base:
        return ishappy(num,base,level+1)
    else:
        return ishappy(num,base,level)
    
def main():
    for case in range(input()):
        bases=map(int,raw_input().split())
        num=1
        while 1:
            num+=1
            flag=True
            for i in range(len(bases)):
                if not ishappy(num,bases[i],0):
                    flag=False
                    break
            if flag:
                print 'Case #%d: %d' % (case + 1, num)
                break;

            

filename=raw_input() #only the filename body without ext
#filename='o'
filein=filename+'.in'
fileout=filename+'.out'
_stdout=sys.stdout
sys.stdin=open(filein,'r')
sys.stdout=open(fileout,'w')
#sys.stdout=Buffer()

main()
sys.stdout=_stdout
print Buffer()
