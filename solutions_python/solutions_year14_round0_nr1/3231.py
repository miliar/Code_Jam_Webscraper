#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import math

def read_matrix(f):
    m = []
    for i in xrange(4):
        m.append(map(int, f.readline().rstrip().split()))
    return m

def read(f):
    n = int(f.readline().rstrip())
    for i in xrange(n):
        a1 = int(f.readline().rstrip())
        m1 = read_matrix(f)
        a2 = int(f.readline().rstrip())
        m2 = read_matrix(f)
        yield a1, m1, a2, m2

def main(f):
    for i, (a1, m1, a2, m2) in enumerate(read(f)):
        candidates = list(set(m1[a1 - 1]).intersection(m2[a2 - 1]))
        if len(candidates) == 1:
            msg = str(candidates[0])
        elif candidates:
            msg = "Bad magician!"
        else:
            msg = "Volunteer cheated!"
        print("Case #{0}: {1}".format(i + 1, msg))

_input = """
3
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 5 4
3 11 6 15
9 10 7 12
13 14 8 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
""".strip()

_output = """
Case #1: 7
Case #2: Bad magician!
Case #3: Volunteer cheated!
""".strip()

def test_main(compare=False):
    import sys
    from difflib import unified_diff
    from StringIO import StringIO

    if compare:
        stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            main(StringIO(_input))
            result = sys.stdout.getvalue().strip()
        finally:
            sys.stdout = stdout

        print(result)

        for line in unified_diff(result.splitlines(), _output.splitlines(),
                                 'Output', 'Expect', lineterm=''):
            print(line)

        if result == _output:
            print("OK")
        else:
            print("NG")

    else:
        main(StringIO(_input))

if __name__ == '__main__':
    test = False
    compare = True
    if test:
        test_main(compare)
    else:
        import sys
        if len(sys.argv) > 1:
            f = open(sys.argv[1])
            main(f)
            f.close()
        else:
            main(sys.stdin)
