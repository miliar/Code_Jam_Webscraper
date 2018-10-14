#!/usr/bin/python

from sys import stdin

def geq(listA, listB):
    a = int(reduce(lambda x,y: str(x)+str(y), listA))
    b = int(reduce(lambda x,y: str(x)+str(y), listB))
    return a>=b

def recursion(target, current, level):
#    print "%s, %s, %d" % (target, current, level)
    if level == len(target)+1:
        return current
    stop = -1
    if len(current) >0:
        stop = current[-1]-1
    for i in range(9, stop, -1):
        if geq(target[:level], current+[i]):
            ret = recursion(target, current+[i], level+1)
            if ret is not None:
                return  ret

def tidy(max_num):
    target_list = [int(x) for x in str(max_num)]
    res = recursion(target_list,[],1)
    return int(reduce(lambda x,y : str(x)+str(y), res))

TESTCASES = int(stdin.readline())
for i in range(1,TESTCASES+1):
    max_num=int(stdin.readline()) 
    res = tidy(max_num)
    print "Case #%d: %s" % (i, res)
