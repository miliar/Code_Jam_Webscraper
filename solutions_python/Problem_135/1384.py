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

def validate(array1, array2):

    result = -1

    for i in array1:
        for j in array2:
            if i == j:
                if result != -1:
                    return "Bad magician!"
                result = i

    if result == -1:
        return "Volunteer cheated!"

    return str(result)

testCount = eval(raw_input())

for test in xrange(1, testCount+1):

    F = eval(raw_input())
    FArray = readrowarray(int(F), int)
    S = eval(raw_input())
    SArray = readrowarray(int(S), int)

    print "Case #%d: %s" % (test, validate(FArray, SArray))



