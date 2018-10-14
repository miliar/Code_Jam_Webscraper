#!/usr/bin/env python
# -*- coding:utf-8 -*-

def numShift(num,i):
    string = str(num)[-i-1:] + str(num)[:-i-1]
    if string[0] == '0':
        return 0
    else:
        return int(string)

def createOneCharNums(m,n):
    returnList = []
    base = ['1','2','3','4','5','6','7','8','9']
    for c in base:
        string = ''
        for i in range(0,len(str(n))):
            string += c
            returnList.append(int(string))
    return returnList


ans = []
loop = int(raw_input())
debug = []

for i in range(loop):
    count = 0
    getList = raw_input().rstrip().split(' ')
    m = int(getList[0])
    n = int(getList[1])
    dataset = range(m,n+1)
    oneCharNumList = createOneCharNums(m,n)
    dataset = sorted(list(set(dataset).difference(set(oneCharNumList))))

    for x in dataset:
        shiftCount = 0
        shifted = 0
        for i in range(len(str(x))-1):
            shifted = numShift(x,shiftCount)
            shiftCount += 1

            if shifted in dataset:
                if x != shifted:
                    count += 1
                    debug.append((x,shifted))
                
    ans.append(count/2)

for i in range(loop):
    print 'Case #%d: '%(i+1) + str(ans[i])
