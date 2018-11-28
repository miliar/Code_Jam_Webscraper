#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function


def read(f):
    n = int(f.readline())
    for i in xrange(n):
        a, b, k = map(int, f.readline().strip().split())
        yield a, b, k


def main(f):
    for i, (a, b, k) in enumerate(read(f)):
        win = 0
        for x in xrange(a):
            for y in xrange(b):
                if x & y < k:
                    win += 1
        print("Case #{0}: {1}".format(i + 1, win))


_input = """
5
3 4 2
4 5 2
7 8 5
45 56 35
103 143 88
""".strip()

_output = """
Case #1: 10
Case #2: 16
Case #3: 52
Case #4: 2411
Case #5: 14377
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
