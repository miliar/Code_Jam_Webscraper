#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import math


def read(f):
    n = int(f.readline().strip())
    for i in xrange(n):
        p, q = map(int, f.readline().strip().split('/'))
        yield p, q


def main(f):
    for i, (p, q) in enumerate(read(f)):
        if 2 ** int(math.log(q) / math.log(2)) != q:
            print("Case #{0}: impossible".format(i+1))
        else:
            n = int(math.ceil((math.log(q) - math.log(p)) / math.log(2)))
            print("Case #{0}: {1}".format(i+1, n))


_input = """
5
1/2
3/4
1/4
2/23
123/31488
""".strip()

_output = """
Case #1: 1
Case #2: 1
Case #3: 2
Case #4: impossible
Case #5: 8
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
    compare = False
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
