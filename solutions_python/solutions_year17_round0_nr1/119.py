import sys

f = open(sys.argv[1], 'r')
T = int(f.readline().rstrip())
for i in xrange(T):
    t = f.readline().split()
    k = int(t[1])
    s = [u for u in t[0]]
    ans = 0
    u = 0
    while u <= len(s) - k:
        while u < len(s) and s[u] == '+':
            u += 1
        if u > len(s) - k:
            break
        #print 'index', u
        for j in xrange(u, u + k):
            if s[j] == '+':
                s[j] = '-'
            else:
                s[j] = '+'
        #print s
        ans += 1
        u += 1
    for v in xrange(u, len(s)):
        if s[v] == '-':
            print 'Case #'+ str(i+1) + ': ' + 'IMPOSSIBLE' 
            break
    else:
            print 'Case #'+ str(i+1) + ': ' + str(ans) 
