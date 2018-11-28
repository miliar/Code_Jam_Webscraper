def solve():    
    r,c  = map(int,raw_input().split())
    a = [list(raw_input()) for _ in xrange(r)]
    for i in xrange(r):
        for j in xrange(c):
            if a[i][j]!='#': continue
            if i==r-1 or j==c-1: return None
            if a[i+1][j]!='#': return None
            if a[i+1][j+1]!='#': return None
            if a[i][j+1]!='#': return None
            a[i][j]=a[i+1][j+1]='/'
            a[i+1][j]=a[i][j+1]='\\'
    return a

t = input()
for tn in xrange(t):
    r = solve()
    print "Case #%d:"%(tn+1)
    if r is None: print "Impossible"
    else: print '\n'.join(''.join(x) for x in r)
