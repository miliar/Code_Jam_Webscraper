#!/usr/bin/python

#Theme Park for Google Code Jam 2009

import sys
import math

def getEuros(R, k, N, groups, case):
    groupsLenght = len(groups)

    size = 0
    euros = 0
    rides = 0
    total = 0
    i = 0

    for i in range (0, groupsLenght):
        total = total + int(groups[i])

    if (total < int(k)):
        euros = total * int(R)
    else:
        i = 0
        while (rides < int(R)):
            index = i % int(N)
            aux = int(size) + int(groups[index])
            if (aux <= int(k)):
                size = aux
                i = i + 1
                euros = euros + int(groups[index])    
            else:
                size = 0
                rides = rides + 1

    print "Case #%d: %d" %  (case, euros)

if len(sys.argv) <> 2:
	print "Correct usage: themepark.py <filename>"
	exit(1)

f = open(sys.argv[1], 'r')
N = f.readline()
i = 2

for line in f:
    if ((i % 2) == 0):
        triple = line
        triple = triple.rstrip('\n')
        R, k, N = triple.split(' ')
    else:
        groups = line
        groups = groups.rstrip('\n')
        groups = groups.split(' ')
        getEuros(R, k, N, groups, (i/2))
    i = i + 1

    
        
