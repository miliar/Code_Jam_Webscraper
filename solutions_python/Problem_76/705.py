'''
Created on May 7, 2011

@author: dan
'''

def PatSum(a, b):
    return a^b

def PatTotal(arr):
    total = 0
    for candy in arr:
        total = PatSum(total, candy)
    return total

def SeanTotal(arr):
    total = 0
    for candy in arr:
        total = total + candy
    return total

def evaluate(pileA, pileB):
    if len(pileA) == 0 or len(pileB) == 0:
        return -1
    if (PatTotal(pileA)!=PatTotal(pileB)):
        return -1
    tot1 = SeanTotal(pileA)
    tot2 = SeanTotal(pileB)
    if (tot1 > tot2):
        return tot1
    return tot2

def recurse(pileA, pileB, remainder):
    if (len(remainder)==0):
        return evaluate(pileA, pileB)
    pileA.append(remainder.pop())
    e1 = recurse(pileA, pileB, remainder)
    pileB.append(pileA.pop())
    e2 = recurse(pileA, pileB, remainder)
    remainder.append(pileB.pop())
    if (e1 > e2):
        return e1
    return e2

def eval(line):
    arr = []
    for word in line.split():
        arr.append(int(word))
    res = recurse([], [], arr)
    if res == -1:
        return "NO"
    return str(res)

import sys
if (len(sys.argv) >1) :
    fname = sys.argv[1]
else:
    fname = "../input.txt"
f = open(fname)
for j in range(int(f.readline())):
    line = f.readline()
    line = f.readline()
    print "Case #"+str(j+1)+": " + eval(line) + ""