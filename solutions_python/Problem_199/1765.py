#!/usr/bin/env python
# encoding: utf-8

def case():
    S, K = raw_input().strip().split()
    S = map(lambda x: x == "+", S)
    K = int(K)

    i = 0
    flips = 0
    while i < len(S) - (K - 1):
        if not S[i]: 
            flips += 1
            for j in xrange(K):
                S[i+j] = S[i+j] ^ True
        i += 1
    if not all(S):
        return "IMPOSSIBLE"
    else:
        return flips


def main():
    T = int(raw_input())
    for i in xrange(1, T + 1):
        print "Case #{}: {}".format(i, case())

if __name__ == "__main__":
    main()
