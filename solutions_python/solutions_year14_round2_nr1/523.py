#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import operator
from collections import defaultdict


def read(f):
    n = int(f.readline().strip())
    for i in xrange(n):
        N = int(f.readline().strip())
        yield [f.readline().strip() for j in xrange(N)]


def parse(s):
    item = []
    for c in s:
        if len(item) > 0 and item[-1][0] == c:
            item[-1][1] += 1
        else:
            item.append([c, 1])
    return item


def calc_move(vals):
    def func():
        for i in xrange(min(vals), max(vals)):
            yield sum(abs(val - i) for val in vals)
    return min(func())


def solve(strings):
    items = map(parse, strings)
    keys = ["".join(map(operator.itemgetter(0), item)) for item in items]
    if len(set(keys)) != 1:
        return None
    n = 0
    for parts in zip(*items):
        vals = map(operator.itemgetter(1), parts)
        if len(set(vals)) == 1:
            continue
        n += calc_move(vals)
    return n


def main(f):
    for i, strings in enumerate(read(f)):
        n = solve(strings)
        if n is None:
            print("Case #{0}: Fegla Won".format(i+1))
        else:
            print("Case #{0}: {1}".format(i+1, n))


_input = """
5
2
mmaw
maw
2
gcj
cj
3
aaabbb
ab
aabb
2
abc
abc
3
aabc
abbc
abcc
""".strip()

_output = """
Case #1: 1
Case #2: Fegla Won
Case #3: 4
Case #4: 0
Case #5: 3
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
