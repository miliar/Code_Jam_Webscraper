import sys, itertools, collections
sys.setrecursionlimit(10000)

read_ints = lambda: map(int, raw_input().split())
read_int  = input

for no_t in xrange(1, read_int() + 1):
    m, n = read_ints()
    s = []
    for i in xrange(m):
        s += [raw_input()]

    mx, cnt = 0, 1
    for a in itertools.product(*[list(xrange(n)) for _ in xrange(m)]):
        if all([i in a for i in xrange(n)]):
            tries = [set() for i in xrange(n)]
            for i, name in enumerate(s):
                tries[a[i]].update(
                    {name[:prefix_len] for prefix_len in xrange(len(name)+1)}
                )
            tot = sum(len(trie) for trie in tries)
            if tot > mx:
                mx, cnt = tot, 1
            elif tot == mx:
                cnt += 1
    print 'Case #%d: %d %d' % (no_t, mx, cnt)
