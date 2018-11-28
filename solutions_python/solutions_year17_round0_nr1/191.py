import sys
t = int(raw_input())
for x in xrange(t):
    sys.stdout.write('Case #{}: '.format(x+1))
    inp = raw_input().split()
    s, k = list(inp[0]), int(inp[~0])
    d = 0
    for i in xrange(0, len(s)-k+1):
        if s[i] == '-':
            for j in xrange(i, i+k):
                s[j] = '+' if s[j] == '-' else '-'
            d += 1
    
    if len(filter(lambda x: x == '-', s)) == 0:
        print d
    else:
        print 'IMPOSSIBLE'