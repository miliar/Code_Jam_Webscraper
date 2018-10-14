#!/usr/bin/env python

def readint(): return int(raw_input())
def readfloat(): return float(raw_input())
def readarray(N, foo):
	res = []
	for i in xrange(N):
		res.append(foo())
	return res
def readlinearray(foo): return map(foo, raw_input().split())
def readrowarray(row, foo):

    for i in xrange(4):
        row -= 1
        temp = raw_input()
        if row == 0:
            result = map(foo, temp.split())

    return result

def runStratgy(C, F, X):

    time = 0
    inc = 2

    while True:

        n_time = C/inc + X/(inc +F)
        c_time = X /inc

        if n_time < c_time:
            time = time + C/inc
            inc = inc + F
        else:
            time = time + c_time
            break

    return time

testCount = eval(raw_input())

for test in xrange(1, testCount+1):

    (C, F, X) = readlinearray(float)

    print "Case #%d: %.7f" % (test, runStratgy(C, F, X))



