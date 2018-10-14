#! /usr/bin/python
from numpy import *
f=open('A-small-attempt0.in')
T=int(f.readline())
for t in range(1,T+1):
    r1 = int(f.readline())
    for i in range(r1-1):
        f.readline()
    r1val =  [int(i) for i in f.readline().split()]
    for i in range(4-r1):
        f.readline()
    r2= int(f.readline())
    for i in range(r2-1):
        f.readline()
    r2val =  [int(i) for i in f.readline().split()]
    for i in range(4-r2):
        f.readline()
    inter = set(r1val)&set(r2val)
    if len(inter)==0:
        print 'Case','#'+str(t)+':','Volunteer cheated!'
    if len(inter)>1:
        print 'Case','#'+str(t)+':','Bad magician!'
    if len(inter)==1:
        print 'Case','#'+str(t)+':',inter.pop()
    inter.clear()
