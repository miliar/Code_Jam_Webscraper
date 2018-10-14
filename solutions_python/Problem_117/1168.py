def col2arr(arr, col):
    tmp = []
    for i in xrange(len(arr)):
        tmp.append(arr[i][col])
    return tmp

t = int(raw_input())
for i in xrange(t):
    n,m = map(int, raw_input().split())
    lawn = [ map(int, raw_input().split()) for _ in xrange(n) ]
    mr = [ max(lawn[j]) for j in xrange(n) ] 
    mc = [ max(col2arr(lawn, j)) for j in xrange(m) ]
    #print mr, mc

    possible = True
    for N in xrange(n):
        for M in xrange(m):
            if lawn[N][M]  not in (mr[N], mc[M]):
                possible = False
                break
    res = "YES" if possible else "NO"
    print "Case #%s: %s" % (i+1, res)
    
