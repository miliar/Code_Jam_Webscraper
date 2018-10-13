#!/usr/bin/env python
import sys
import fractions

def solve(*numbers):
    minimum = min(numbers)
    differences = map(lambda x: x - minimum, numbers) 
    T = reduce(fractions.gcd, differences)
    if minimum % T == 0:
        return 0
    return T - (minimum % T)

def main():
    i = 0
    results = []
    N = int(sys.stdin.readline())
    for line in sys.stdin:
        print "Case #%d: %d" % (i + 1, solve(*map(long, line.split()[1:])), )
        i = i + 1
        if i >= N:
            break

if __name__ == '__main__':
    main()
