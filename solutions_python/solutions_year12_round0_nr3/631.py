import sys
vals = {}
for v in xrange(1, 2000005):
    if v % 1000 == 0:
        print >> sys.stderr, v
    vals[v] = set()
    s = str(v)
    for i in xrange(1, len(s)):
        ns = s[i:]+s[:i]
        if ns[0] == '0':
            continue
        if int(ns) <= v:
            continue
        vals[v].add(int(ns))
print >> sys.stderr, "done"

T = int(raw_input())

for case in xrange(1, T+1):
    A, B = map(int, raw_input().split())
    ans = 0

    for n in xrange(A, B):
        for m in vals[n]:
            if m <= B:
                ans += 1

    print "Case #%d: %d"%(case, ans)
    print >> sys.stderr, "Case #%d: %d"%(case, ans)

