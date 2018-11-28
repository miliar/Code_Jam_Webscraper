#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Google Code Jam: Round 1B 2016
# Problem B. Close Match
#
# by xenosoz on May 1, 2016.
#

T = int(input())

def cmp(lhs, rhs):
    return -(lhs<rhs) + (lhs>rhs)

def score(item):
    C, J = item
    c, j = int(C), int(J)
    return (abs(c-j), c, j)

def make_min(S):
    return S.replace("?", "0")

def make_max(S):
    return S.replace("?", "9")

def solve(C, J):
    if not C or not J:
        return ("", "")
    
    solns = []

    c, j = head_c, head_j = C[0], J[0]
    tail_c_min = make_min(C[1:])
    tail_c_max = make_max(C[1:])
    tail_j_min = make_min(J[1:])
    tail_j_max = make_max(J[1:])
    
    if c == "?" and j == "?":
        tail_c_next, tail_j_next = solve(C[1:], J[1:])
        solns.append(("0" + tail_c_next, "0" + tail_j_next))
        solns.append(("0" + tail_c_max, "1" + tail_j_min))
        solns.append(("1" + tail_c_min, "0" + tail_j_max))
    elif c == "?":
        tail_c_next, tail_j_next = solve(C[1:], J[1:])
        solns.append((j + tail_c_next, j + tail_j_next))
        if j != "0":
            solns.append((str(int(j)-1) + tail_c_max, j + tail_j_min))
        if j != "9":
            solns.append((str(int(j)+1) + tail_c_min, j + tail_j_max))
    elif j == "?":
        tail_c_next, tail_j_next = solve(C[1:], J[1:])
        solns.append((c + tail_c_next, c + tail_j_next))
        if c != "0":
            solns.append((c + tail_c_min, str(int(c)-1) + tail_j_max))
        if c != "9":
            solns.append((c + tail_c_max, str(int(c)+1) + tail_j_min))
    else:
        if c == j:
            tail_c_next, tail_j_next = solve(C[1:], J[1:])
            solns.append((c + tail_c_next, j + tail_j_next))
        if c > j:
            solns.append((c + tail_c_min, j + tail_j_max))
        if c < j:
            solns.append((c + tail_c_max, j + tail_j_min))
    return sorted(solns, key=score)[0]


for t in range(1, T+1):
    C, J = input().split()
    assert len(C) == len(J)
    
    AC, AJ = solve(C, J)
    JJ, CC = solve(J, C)
    assert AC == CC and AJ == JJ

    print("Case #%d: %s %s" % (t, AC, AJ))
