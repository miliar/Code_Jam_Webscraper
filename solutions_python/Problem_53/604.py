#!/usr/bin/python

import sys

def getsol(t, n, k):
    try:
        if bin(k)[2:][::-1][:n]==bin(2**n-1)[2:]:
            print 'Case #'+str(t)+': ON'
        else:
            print 'Case #'+str(t)+': OFF'   
    except:
        print 'Case #'+str(t)+': OFF'


data = sys.stdin.readlines()
data.remove(data[0])

t=0

for line in data:
    t+=1
    actr = line.strip().split(' ')
    getsol(t,int(actr[0]),int(actr[1]))
