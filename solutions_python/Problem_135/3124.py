#!/usr/bin/python

from sys import stdin

def solve():
    row = int(stdin.readline())
    s1 = [ list(map(int, stdin.readline().split())) for i in range(4) ][row - 1]
    row = int(stdin.readline())
    s2 = [ list(map(int, stdin.readline().split())) for i in range(4) ][row - 1]
    s1 = set(s1)
    s2 = set(s2)
    s = s1.intersection(s2)
    if len(s) == 0:
        return 'Volunteer cheated!'
    if len(s) > 1:
        return 'Bad magician!'
    return list(s)[0]


t = int(stdin.readline())
for i in range(t):
    print('Case #%d:' % (i + 1), solve())


