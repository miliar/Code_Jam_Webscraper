#! /usr/bin/python

import sys
import re

L = 0
D = 1
N = 2

words = []
testCases = []

    

input = open(sys.argv[1])

'''
The first line of input contains 3 integers, L, D and N separated by a space. 
D lines follow, each containing one word of length L. These are the words that 
are known to exist in the alien language. N test cases then follow, each on its 
own line and each consisting of a pattern as described above. You may assume that 
all known words provided are unique.
'''
line = input.readline()
paramsArr = line.split()

# get words in dictionary
for i in range(int(paramsArr[D])):    
    line = input.readline()
    words.append(line[:int(paramsArr[L])])

# get test cases
for i in range(int(paramsArr[N])):    
    line = input.readline().rstrip()
    testCases.append(line)

reg = re.compile("\(\w*\)")
for c in range(int(paramsArr[N])):
    matchCount = 0
    tc = testCases[c]
    start = 0
    matchArr = []
    while(len(tc[start:]) != 0):
        match = reg.match(tc[start:])
        
        if match:
            matchArr.append((start,start + match.end()))
            start = start + match.end()
        else:
            matchArr.append((start,start + 1))
            start += 1

    for w in words:
        for idx in range(int(paramsArr[L])):
            matchFlag = 1
            
            #print "test", w, w[idx], "=", tc[matchArr[idx][0]:matchArr[idx][1]]
            if w[idx] not in tc[matchArr[idx][0]:matchArr[idx][1]]:
                matchFlag = 0
                #print w[idx], "not in matching section"
                break
                    
        if(matchFlag == 1):
            matchCount += 1
            #print w, "is a match", tc
            #print "next word"

    print "CASE #" + str(c+1) + ":", matchCount




