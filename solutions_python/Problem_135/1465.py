#!/usr/bin/env python

import sys


N = 4


if __name__ == '__main__':
    T = int(sys.stdin.readline())

    for i in range(T):
        a = int(sys.stdin.readline())
        row_a = None
        
        for j in range(N):
            if j + 1 == a:
                row_a = set(map(int, sys.stdin.readline().split()))
            else:
                sys.stdin.readline()
        
        b = int(sys.stdin.readline())
        row_b = None
        
        for j in range(N):
            if j + 1 == b:
                row_b = set(map(int, sys.stdin.readline().split()))
            else:
                sys.stdin.readline()
        
        
        intersection = row_a & row_b
        
        if len(intersection) == 0:
            print('Case #%d: Volunteer cheated!' % (i + 1))
        elif len(intersection) == 1:
            print('Case #%d: %d' % (i + 1, intersection.pop()))
        else:
            print('Case #%d: Bad magician!' % (i + 1))
