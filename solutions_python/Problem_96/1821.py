#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      particle.mania
#
# Created:     14-04-2012
# Copyright:   (c) particle.mania 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

if __name__ == '__main__':
    main()

from math import *

fil=open('C:\Users\particle.mania\Documents\Portable Python 2.7.2.1\inputjam.txt','r')
f = fil.readlines()

FS=f[1:]

i=1

for l in FS:
    #print l[3:]
    total = map(int,l.split()[3:])
    level = int(l.split()[2])
    free = int(l.split()[1])
    idbest = map(lambda x: int((x+2)/3), total)
    #print idbest
    ans1 = len(filter(lambda x: x>=level, idbest))
    ans2 = min(len(filter(lambda x: x==level-1 and x!=0, idbest)), free)
    print 'Case #'+str(i)+': '+str(ans1+ans2)
    i=i+1

