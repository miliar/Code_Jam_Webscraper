import sys

lines = sys.stdin.readlines()
n = int(lines[0])
assert len(lines) == n+1
for i in xrange(n):
    s, k = lines[i+1].strip().split()
    k = int(k)
    s = [x for x in s]
    cnt = 0
    for j in xrange(len(s)-k+1):
        if s[j] == '-':
            for t in xrange(k):
                s[j+t] = chr(ord('-') + ord('+') - ord(s[j+t]))
            cnt += 1
    ok = (s.count("-") == 0)
    print "Case #%d: %s" % (i+1, str(cnt) if ok else "IMPOSSIBLE")
    
