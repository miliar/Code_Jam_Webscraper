#!/usr/bin/env python
# encoding: utf-8

def case():
    N, K = map(int, raw_input().split())
    L = [N]
    for i in xrange(K):
        a = L.pop(L.index(max(L)))
        b = a // 2
        c = a - b - 1
        L += [b, c]
    return " ".join(map(str,[b, c]))


def main():
    T = int(raw_input())
    for i in xrange(1, T + 1):
        print "Case #{}: {}".format(i, case())

if __name__ == "__main__":
    main()
