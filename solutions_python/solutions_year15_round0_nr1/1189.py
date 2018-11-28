#!/usr/bin/python

'''
Google Code Jam 2015
By gweizman@gmail.com
'''
import sys

if len(sys.argv) != 3:
    print 'Usage: python shyness.py <input> <output>'
    sys.exit(0)
    
f = open(sys.argv[1], 'r')
o = open(sys.argv[2], 'w')

f.readline() # Skip first line
case = 1
for line in f:
    spectators = 0
    sum = 0
    words = line.split()
    for i,people in enumerate(list(words[1])):
        spectators += max(0, (i - sum - spectators))
        sum += int(people)
    o.write("Case #" + str(case) + ": " + str(spectators) + "\n")
    case += 1
    
