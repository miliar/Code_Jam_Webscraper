#!/usr/env/python
# coding: utf-8
# 
 
import sys
 
f = open("./A-large.in")
out = open("./A-large.out", 'w')

T = f.readline()

for index,line in enumerate(f):
    friends = 0
    cur_standings = 0
    tmp = line.strip('\n').split(' ')
    L = int(tmp[0])
    s = tmp[1]
    for i in xrange(L+1):
        if s[i]>'0':
            if cur_standings<i:
                friends += (i-cur_standings)
                cur_standings = i + int(s[i])
            else:
                cur_standings += int(s[i])
        else:
            pass
    out.write('Case #'+str(index+1)+': '+str(friends)+'\n')

f.close()
out.close()
