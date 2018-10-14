#!/usr/bin/env python
# encoding: utf-8

def case():
    N = map(int, raw_input().strip())
    for i in xrange(len(N)-1, 0, -1):
        if any(map(lambda x: x > N[i], N[:i])):
            for j in range(i, len(N)):
                N[j] = 9
            N[i-1] = N[i-1] - 1
    return "".join(map(str,N)).lstrip("0")

def main():
    T = int(raw_input())
    for i in xrange(1, T + 1):
        print "Case #{}: {}".format(i, case())

if __name__ == "__main__":
    main()
