#!/usr/bin/env python

import sys
import os

ERR = ['Bad magician!', 'Volunteer cheated!'] 

def solve(t):
    n = int(sys.stdin.readline())
    r1 = []
    for i in range(1, 5):
        if i is n:
            r1 = map(int, sys.stdin.readline().split())
        else:
            sys.stdin.readline()

    n = int(sys.stdin.readline())
    r2 = []
    for i in range(1, 5):
        if i is n:
            r2 = map(int, sys.stdin.readline().split())
        else:
            sys.stdin.readline()

    matched_num = 0
    card = 0
    for e1 in r1:
        if e1 in r2:
            matched_num += 1
            card = e1

    answer = 'Case #{0}: '.format(t)
    if matched_num is 0:
        answer += ERR[1]
    elif matched_num is 1:
        answer += str(card)
    else:
        answer += ERR[0]

    print answer

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for t in range(1, T + 1):
        solve(t)
