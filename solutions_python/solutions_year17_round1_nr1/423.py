#!/usr/bin/env python

import sys
case = 0
def print_results(*args,**kwargs):
    print 'Case #'+str(case)+': '
    for e in args[0]:
        print ''.join(e)
def solution(R,C,cake):
    #print cake
    res = [[] for i in range(R)]
    index =  1;last= 0;flag2 =True
    for i,x in enumerate(cake):
        flag = True;last = -1
        for j,y in enumerate(x):
            if y=='?':continue
            flag = False
            res[i]+=[y for p in range(j-last)]
            last = j
        if flag:
            if flag2: last+=1
            res[i] = res[i+index]
        else:
            if flag2:
                for k in range(i):
                    res[k]=res[i]
            flag2 = False
            index = -1
            res[i]+=[res[i][last]]*(C-1-last)
    print_results(res)
testcases = int(sys.stdin.readline())

for i in range(testcases):
    case += 1
    R,C = sys.stdin.readline().split()
    R = int(R);C=int(C)
    temp = []
    for j in range(R):
        temp.append(list(sys.stdin.readline()[:C]))
    solution(R,C,temp)
