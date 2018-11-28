#!/usr/bin/python
import sys


def main():
    lineno = 0
    for line in sys.stdin:
        lineno += 1
        if lineno == 1:
            continue
        if lineno % 2 == 0:
            continue
        ary = map(int, line.split(" "))
        ary.sort()
        xor_sum = 0
        for i in ary:
            xor_sum ^= i
        print "Case #%d:" % (lineno / 2),
        if xor_sum == 0:
            print sum(ary) - ary[0]
        else:
            print "NO"

if __name__ == '__main__':
    main()
