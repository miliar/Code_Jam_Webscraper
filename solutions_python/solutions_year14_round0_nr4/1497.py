#!/usr/bin/python

def deceitful(Naomi, Ken):
    Naomi.sort()
    Ken.sort()
    score = 0
    k = Ken.pop(0)
    for n in Naomi:
        if n>k:
            score += 1
            if len(Ken)>0:
                k = Ken.pop(0)
    return score

def war(Naomi, Ken):
    Naomi.sort()
    Naomi.reverse()
    Ken.sort()
    Ken.reverse()
    score = 0
    k = Ken.pop(0)
    for n in Naomi:
        if n>k:
            score += 1
        else:
            if len(Ken)>0:
                k = Ken.pop(0)
    return score

def readFloats(): return [float(i) for i in raw_input().split()]

for test in range(int(raw_input())):
    N = int(raw_input())
    Naomi = readFloats()
    Ken = readFloats()

    print 'Case #%d:' % (test+1), deceitful(list(Naomi), list(Ken)), war(list(Naomi), list(Ken))
