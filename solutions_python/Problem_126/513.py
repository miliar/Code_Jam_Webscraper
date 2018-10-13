#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, time

vocals = ['a', 'e', 'i', 'o', 'u']

def substr(string, n):
    j=n
    a=list()
    while True:
        for i in range(len(string)-j+1):
            a.append(string[i:i+j])
        if j==len(string):
            break
        j+=1
        #string=string[1:]
    return a

def consecutiveConsonants(string):
    counting = False
    num = 0
    max = 0
    for i in range(len(string)):
        if string[i] not in vocals:
            num += 1
            if not counting:
                counting = True
        else:
            if counting:
                if num > max:
                    max = num
                num = 0
                counting = False
    if num > max:
        max = num
    return max  

def nValue(name, n):
    substrings = substr(name, n)
    result = 0
    for sub in substrings:
        if consecutiveConsonants(sub) >= n:
            result += 1
    return str(result)

startTime = time.time()
f = open(sys.argv[1])
outF = open(sys.argv[1].split('.')[0] + '.out', 'w')
lines = f.readlines()
f.close()
for i in range(0, (int(lines[0]))):
    values = lines[i+1].split(' ')
    #result = 'Case #' + str(i+1) + ': ' + nValue(values[0], int(values[1]))
    #print result
    print >> outF, 'Case #' + str(i+1) + ':', nValue(values[0], int(values[1]))
print '%f seconds elapsed' % (time.time() - startTime)