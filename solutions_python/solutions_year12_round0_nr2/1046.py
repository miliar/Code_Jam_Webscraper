#!/usr/bin/env python

Sample = False

plain = [(0, 0, 0)] * 31
surprise = [(0, 0, 0)] * 31
# excessoes
surprise[0] = 0
surprise[1] = 0
surprise[29] = 0
surprise[30] = 0
def Decompose(n):
    for i in range(0, 11):
        for j in range(i, min(i+3,11)):
            for k in range(j, min(i+3,11)):
                if i+j+k == n:
                    if Sample: print n,i,j,k
                    if k - i < 2:
                        plain[n] = (i, j, k)
                        plain[n] = k
                    else:
                        surprise[n] = (i, j, k)
                        surprise[n] = k

def Better(p, surprises, scores):
    count = 0
    for each in scores:
        if plain[each] >= p:
            count += 1
        elif (surprises > 0) and (surprise[each] >= p):
            count += 1
            surprises -= 1
    return count

for n in range(0, 31):
    Decompose(n)

if Sample:
    print plain
    print surprise

    for n in range(0, 31):
        print "%d, (%d, %d, %d), (%d, %d, %d)" % (n, plain[n][0], plain[n][1], plain[n][2], surprise[n][0], surprise[n][1], surprise[n][2])

testCases = int(input())
for no in range(1, testCases+1):
    line = raw_input()
    #print "line", line
    line = line.split()
    #print "new line", line
    values = map(int, line)
    N = values[0]
    S = values[1]
    p = values[2]
    scores = values[3:]
    count = Better(p, S, scores)
    #print N, S, p, count
    print "Case #%d: %d" % (no, count)
