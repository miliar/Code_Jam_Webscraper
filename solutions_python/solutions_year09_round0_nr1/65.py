#!/usr/bin/env python

import sys

def main():
    L, D, N = [int(v) for v in sys.stdin.readline().strip().split()]
    words = [
        sys.stdin.readline().strip() for i in range(D)
    ]
    patterns = [
        sys.stdin.readline().strip() for i in range(N)
    ]

    test_case = 1
    for pattern in patterns:
        aux = []
        while len(pattern):
            if pattern[0] == '(':
                aux.append(set(pattern[1:pattern.find(")")]))
                pattern = pattern[pattern.find(")") + 1:]
            else:
                aux.append(set(pattern[0]))
                pattern = pattern[1:]

        count = 0
        for word in words:
            good = True
            for pos in range(len(word)):
                if word[pos] not in aux[pos]:
                    good = False
                    break
            if good:
                count += 1
        print "Case #%d: %d" % (test_case, count)
        test_case += 1
    return 0

if __name__ == "__main__":
    main()

