"""Recycled numbers"""

import sys


cycled = {}

def cycles(num):
    num = str(num)
    if num in cycled:
        for c in cycled[num]:
            yield c
        return
    cache = set()

    # drop out early
    if len(set(num)) == 1:
        yield int(num)
        cycled[num] = set([int(num)])
        return

    l = len(num)
    idxs = [i for i in xrange(l) if num[i] >= num[0] and num[i] != '0']
    done = set()
    for i in idxs:
        c = num[i:] + num[:i]
        if c in done:
            next
        done.add(c)
        int_c = int(c)
        cache.add(int_c)
        yield int_c
    cycled[num] = cache

def decide(input):
    """Given integers A and B with the same number of digits and no leading zeros,
    how many distinct recycled pairs (n, m) are there with A <= n < m <= B?"""
    a, b = [int(i) for i in input.split()]
    recycled = set()

    for n in xrange(a, b+1):
        for m in cycles(n):
            if n < m <= b:
                recycled.add((n, m))

    return len(recycled)


def run(infile):
    f = open(infile)
    num = int(f.readline())
    for i in xrange(num):
        line = f.readline().strip()
        print 'Case #{count}: {}'.format(decide(line), count=i+1)


if __name__ == '__main__':
    run(sys.argv[1])
