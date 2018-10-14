#! /usr/bin/python
def cycle_count(n, B):
    result = set()
    for i in range(1, len(str(n))):
        m = n[i:] + n[:i]
        if n < m <= B:
            result.add((n, m))
    return result

def solve(A, B):
    result = set()
    for i in range(int(A), int(B)+1):
        result.update(cycle_count(str(i), B))
    return result

def solve2(A, B):
    result = set()
    for i in range(A, B):
        for j in range(i+1, B):
            if cyckepair(i, j):
                result.add(i, j)
    return result

T = input()
for c in range(1, T+1):
    A, B = raw_input().split()
    print "Case #%d: %d" % (c, len(solve(A, B)))
    
