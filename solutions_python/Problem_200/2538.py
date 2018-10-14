#!/usr/bin/python

n = int(raw_input())

def tidy(n):
    sn = str(n)
    start = 0
    for i in xrange(len(sn) - 1):
        if int(sn[i + 1]) < int(sn[i]):
            return False
    return True

def bop(n):
    sn = str(n)
    start = 0
    bo = 0
    for i in xrange(len(sn) - 1):
        if int(sn[i + 1]) < int(sn[i]):
            return len(sn) - bo - 1
        elif int(sn[i + 1]) > int(sn[i]):
            bo = i + 1
    return None

def htidy(n):
    if tidy(n):
        return n
    else:
        return n - (n % (10 ** bop(n))) - 1

for i in xrange(n):
    print "Case #" + str(i + 1) + ": " + str(htidy(int(raw_input())))

