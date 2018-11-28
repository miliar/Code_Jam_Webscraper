#!/usr/bin/env python
#gabriel pettier


file = open('B-small.in')

N = int(file.readline().split('\n')[0])

def cmpr(d1, d2):
    for i in d1:
        if i not in d2 or d2[i] != d1[i]:
            return False
    for i in d2:
        if i not in d1 or d2[i] != d1[i]:
            return False
    return True

def digit(n):
    digits = {}
    for i in n:
        if i is not '0':
            if i in digits:
                digits[i] += 1
            else:
                digits[i] = 1
    return digits

i = 0
for line in file.readlines():
    i += 1
    num = line.split('\n')[0]

    NUM= int(num)
    d=digit(num)

    next = NUM+1
    while not cmpr(d, digit(str(next))):
        next += 1

    print 'Case #'+str(i)+': '+str(next)
