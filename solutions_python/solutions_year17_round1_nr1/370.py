#!/usr/bin/python

from collections import deque

def ir():
    return int(raw_input())

def ia():
    line = raw_input()
    line = line.split()
    return map(int, line)

def fill_n():
    global R, C, M
    n, m  = R, C
    for i in range(n):
        j = 0
        while j < m and M[i][j] == '?': j += 1 # first one
        if j == m: continue
        c = M[i][j]
        # go back and fill
        while j >= 0: M[i][j] = c; j -= 1

        for j in range(m):
            if      M[i][j] == '?': M[i][j] = c; j += 1
            else                  : c = M[i][j]; j += 1

def fill_m():
    global R, C, M
    n, m  = R, C
    
    for j in range(m):
        i = 0
        while i < n and M[i][j] == '?': i += 1 # first one
        if i == n: continue
        c = M[i][j]
        # go back and fill
        while i >= 0: M[i][j] = c; i -= 1

        for i in range(n):
            if      M[i][j] == '?': M[i][j] = c; i += 1
            else                  : c = M[i][j]; i += 1
            
def solve0():
    global R, C, M
    n, m  = R, C
    fill_n()
    fill_m()

def solve():
    global R, C, M
    R, C = ia()
    M = []
    for i in xrange(R): M.append(list(raw_input()))

    solve0()

    ans = ""
    for c in M:
        ans = ans + "\n" + "".join(c)
    return ans

T = ir()
for it in xrange(1, T + 1):
    ans = solve()
    print "Case #%d:" % it, ans
