#!/usr/bin/python2

parts = []
for i in range(1, 21):
    parts.append(int('1' * i))
parts = parts[::-1]

def solve():
    n = int(raw_input())
    tidy = 0
    for i in parts:
        while tidy+i <= n and ((tidy / 10**(len(str(i))-1)) % 10 < 9):
            tidy += i
    return tidy

T = int(raw_input())
for i in range(T):
    print "Case #%d:" % (i+1), solve()
