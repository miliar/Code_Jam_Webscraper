#!/usr/bin/python

import sys

n = int(sys.stdin.readline())

#target = 'welcome to code jam'

def myfind(pattern, str):
    if len(str) == 1:
        if pattern == str: return 1
        else: return 0
    count = 0
    findchar = pattern[0]

    begin_indexs = []
    index = -1
    while (True):
        index = str.find(findchar, index+1) # next nextchar
        if (index == -1): break
        else:             begin_indexs.append(index)

    if len(pattern) == 1:
        return len(begin_indexs)
    return sum([ myfind(pattern[1:], str[index+1:]) for index in begin_indexs])
            


target = 'welcome to code jam'
for case in xrange(1, n+1):
    line = ''.join([ch for ch in list(sys.stdin.readline()) if ch in target ])
    line = line[line.find(target[0]):]

    answer = myfind(target, line)
    print 'Case #%d: %04d'%(case, answer)


