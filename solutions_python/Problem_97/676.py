from collections import defaultdict

M = defaultdict(lambda: set())
for j in xrange(1,2000000):
    s = str(j)
    for k in xrange(1,len(s)):
        if s[k] != '0':
            recycled = int(s[k:] + s[:k])
            if recycled > j:
                M[j].add(recycled)

T = int(raw_input())
for i in xrange(T):
    total = 0
    (A,B) = map(int,raw_input().split())
    for j in xrange(A,B+1):
        total += len([m for m in M[j] if m <= B])
    print 'Case #%d: %d' % (i+1,total)
