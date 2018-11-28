#!/usr/bin/env python

from __future__ import division

from StringIO import StringIO
import sys

INPUT = '''3
1 100 50
10 10 100
9 80 56
'''

OUTPUT = '''Case #1: Possible
Case #2: Broken
Case #3: Possible
'''

def is_integral(n):
    return n-int(n) == 0

def main(stdin, stdout):
    def possible(i):
        stdout.write('Case #{0}: Possible\n'.format(i))

    def not_possible(i):
        stdout.write('Case #{0}: Broken\n'.format(i))

    stdin.next()  # Skip the first line
    for i, line in enumerate(stdin, 1):
        n, p1, p2 = line.split()
        n, p1, p2 = int(n), int(p1), int(p2)

        if p1 == 100 and p2 == 100:
            possible(i)
            continue

        if p1 != 100 and p2 == 100:
            not_possible(i)
            continue

        if p1 == 0 and p2 == 0:
            possible(i)
            continue

        if p1 != 0 and p2 == 0:
            not_possible(i)
            continue

        if n >= 100:
            possible(i)
            continue

        is_possible = False

        for q in range(1, n+1): 
            if is_integral(q*p1/100):
                is_possible = True
                break

        if is_possible:
            possible(i)
        else:
            not_possible(i)

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'test':
        output = StringIO()
        main(StringIO(INPUT), output)
        output.seek(0)
        output = output.read()
        assert output == OUTPUT, '{0} != {1}'.format(output, OUTPUT)
        print "OK"
    elif len(sys.argv) == 2 and sys.argv[1] == 'calc':
        calc()
    else:
        main(sys.stdin, sys.stdout)
