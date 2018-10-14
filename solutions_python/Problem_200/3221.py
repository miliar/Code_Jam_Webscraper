#!/usr/bin/env python
#-*-coding: utf-8 -*-

def readint(): return int(raw_input())
def readarray(f): return map(f, raw_input().split())

T = readint()

def get_index(l):
    for i in range(len(l)):
        n = l[i]
        for j in range(i+1,len(l)):
            if l[j] < n:
                return i
    return -1

for t in range(T):
    l = [int(c) for c in raw_input()]
    index = get_index(l)
    if index == -1:
        print "Case #%d: %s" % (t + 1, ''.join(map(str,l)))
    else:
        i = index
        while l[i + 1] > l[index]:
            i += 1
            if i + 1 == len(l):
                if l[index] != 1:
                    l[index] -= 1
                    for j in range(index+1, len(l)):
                        l[j] = 9
                else:
                    for j in range(index, len(l)):
                        l[j] = 9
                    if index == 0:
                        l = l[1:]
                print "Case #%d: %s" % (t + 1, ''.join(map(str,l)))
                break
        l[i] -= 1
        for j in range(i + 1, len(l)):
            l[j] = 9
        if l[0] == 0:
            l = l[1:]
        print "Case #%d: %s" % (t + 1, ''.join(map(str,l)))
