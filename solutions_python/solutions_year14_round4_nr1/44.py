#!/usr/bin/pypy

def read_line():
    s = raw_input()
    while s == "":
        s = raw_input()
    return s

def read_int():
    return int(read_line())

def read_ints():
    return tuple(int(s) for s in read_line().split())

def solve():
    N, X = read_ints()
    S = read_ints()
    S = tuple(sorted(S))

    assert len(S) == N
    pairs = 0
    i = N - 1
    while i > pairs:
        if S[i] + S[pairs] <= X:
            pairs += 1
        i -= 1
    return N - pairs

if __name__ == "__main__":
    T = int(read_line())
    for i in range(1, T+1):
        solution = solve()
        print "Case #{0}: {1}".format(i, solution)
