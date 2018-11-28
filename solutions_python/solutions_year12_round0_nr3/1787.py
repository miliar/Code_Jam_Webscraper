#!/usr/bin/env python

from __future__ import with_statement

def foo(A, B):
    d = {}
    for n in range(A, B):
        for m in range(A+1, B+1):
            if n < m:
                s = str(n)
                combs = [int(s[i:] + s[:i]) for i in range(1, len(s))]
                for c in combs:
                    if c == m:
                        if not "%s%s" % (n, m) in d:
                            d.update({ "%s%s" % (n, m): None })

    count = 0
    for k in d:
        count += 1

    return count

def main(argv):
    if len(argv) == 2:

        lines = []

        with open(argv[1]) as f:
            for line in f.readlines():
                lines.append(line[:-1])

        T = int(lines[0])
        lines = lines[1:]
        if not len(lines) == T:
            raise Exception("Wrong number of input lines.")

        i = 1
        for line in lines:
            A = int(line.split(" ")[0])
            B = int(line.split(" ")[1])

            print "Case #%s: %s" % (i, foo(A, B))
            i += 1

    else:
        print "Usage: ./problem_b.py input.txt"

if __name__ == '__main__':
    from sys import argv
    main(argv)


