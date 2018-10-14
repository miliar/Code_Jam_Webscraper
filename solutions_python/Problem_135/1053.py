#!/usr/bin/env python

def getCase():
    answer = int(raw_input())
    suspect = []
    for row in range(1, 1 + 4):
        if row == answer:
            suspect = set(map(int, raw_input().split()))
        else:
            raw_input()
    return suspect

T = int(raw_input())
for t in range(T):
    common = list(getCase() & getCase())
    l = int(len(common))
    if l == 1:
        answer = int(common[0])
    elif l > 1:
        answer = 'Bad magician!'
    elif l < 1:
        answer = 'Volunteer cheated!'
    print 'Case #{0}: {1}'.format(t + 1, answer)
