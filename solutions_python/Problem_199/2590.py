t = int(raw_input())

def flip(x, i, k):
    for j in xrange(k):
        x[i+j] = '+' if x[i+j] == '-' else '-'
    

for c in xrange(t):
    x, k = raw_input().split()
    x = list(x)
    k = int(k)
    lx = len(x)
    count = 0
    for i in xrange(lx-k+1):
        if (x[i] == '-') :
            flip(x, i, k)
            count += 1
    
    val = "IMPOSSIBLE" if ('-' in x) else str(count)
    print "Case #%d: %s" % (c+1, val)