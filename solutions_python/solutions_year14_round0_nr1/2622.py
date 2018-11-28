#!/usr/bin/env python

def readRow(row):
    P = {}
    for x in range(1,5):
        if row == x:
            P = map(int, raw_input().split())
        else:
            raw_input()
    return P

N = int(raw_input())
for t in range(N):
    A1 = int(raw_input())
    P = readRow(A1)
    A2 = int(raw_input())
    Q = readRow(A2)

    result = list(set(P).intersection(Q))
    print 'Case #%d:' % (t+1) , 
    res = len(result)
    if res == 0:
        print 'Volunteer cheated!'
    elif res == 1:
        print result[0]
    else:
        print 'Bad magician!'


