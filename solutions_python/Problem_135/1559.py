#!/usr/bin/python

def solve(row1, M1, row2, M2):
    candidates = set(M1[row1]).intersection(set(M2[row2]))
    if len(candidates)==0:
        return "Volunteer cheated!"
    elif len(candidates)==1:
        return candidates.pop()
    else:
        return "Bad magician!"

def readInts(): return [int(i) for i in raw_input().split()]

for test in range(int(raw_input())):
    row1 = int(raw_input())-1
    M1 = []
    for i in range(4):
        M1.append(readInts())
    row2 = int(raw_input())-1
    M2 = []
    for i in range(4):
        M2.append(readInts())

    print 'Case #%d:' % (test+1), solve(row1, M1, row2, M2)
