import sys, itertools, collections
sys.setrecursionlimit(10000)

read_ints = lambda: map(int, raw_input().split())
read_int  = input


def gao(n, k):
    ups = collections.defaultdict(list)
    def compute_up(x):
        if x in ups:
            return

        l = x / 2
        r = x - 1 - l
        if l > 0:
            compute_up(l)
            ups[l].append(x)
        if r > 0:
            compute_up(r)
            ups[r].append(x)
    compute_up(n)

    counts = {}
    def compute_count(x):
        if x in counts:
            return counts[x]

        if x == n:
            counts[x] = 1
        else:
            counts[x] = sum(compute_count(u) for u in ups[x])
        return counts[x]
    compute_count(1)

    assert sum(counts.itervalues()) == n, '!!!'

    for key, value in sorted(counts.iteritems(), key=lambda item: -item[0]):
        k -= value
        if k <= 0:
            return '%d %d' % (key / 2, key - 1 - key / 2)

    raise


for no_t in xrange(1, read_int() + 1):
    n, k = read_ints()
    print 'Case #%d: %s' % (no_t, gao(n, k))
