#!/usr/bin/python

'''
Google Code Jam 2015
By gweizman@gmail.com
'''
import sys

if len(sys.argv) != 3:
    print 'Usage: python mushroom.py <input> <output>'
    sys.exit(0)
    
f = open(sys.argv[1], 'r')
o = open(sys.argv[2], 'w')

f.readline() # Skip first line
case = 1
for line in f:
    input = next(f).rstrip() # Skip first line
    words = map(int, input.split())
    last_num = words[0]
    max_diff = 0
    first_method = 0
    second_method = 0
    for i in words:
        first_method += max(last_num - i, 0)
        max_diff = max(max_diff, last_num - i)
        last_num = i
    for i in words[:-1]:
        second_method += min(i, max_diff)
    o.write("Case #" + str(case) + ": " + str(first_method) + " " + str(second_method) + "\n")
    case += 1
    
