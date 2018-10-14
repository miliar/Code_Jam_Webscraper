__author__ = 'linusyang'

import fileinput
import itertools

s2i = lambda xs : [int(x) for x in xs]

def comb(ds):
    result = set()
    for i in xrange(len(ds)):
        result |= set([sum(x) for x in itertools.combinations(ds, i + 1)])
    return result

def solve(c, v, ds):
    total = set(range(1, v + 1))
    left = total - comb(ds)
    result = 0
    while left:
        x = min(left)
        newones = set([x] + [i + x for i in total - left])
        left -= newones
        result += 1
    return result

def main():
    f = fileinput.input()
    count = int(f.readline())
    for i in xrange(1, count + 1):
        c, d, v = tuple(s2i(f.readline().split()))
        ds = s2i(f.readline().split())
        print("Case #%d: %d" % (i, solve(c, v, ds)))

if __name__ == '__main__':
    main()
