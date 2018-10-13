
T = int(raw_input())
for c in xrange(T):
    A, B = map(int, raw_input().strip().split())
    print "Case #%d:"%(c+1),
    count = 0
    for x in xrange(A,B+1):
        s, st = str(x), set()
        for i in xrange(len(s)):
            n = int(s[i:]+s[:i])
            if A<=n<=B and n<x: st.add(n)
        count += len(st)
    print count
    
