def prettyPrint( lawn ):
    for k in xrange(len(lawn)):
        print ""
        for l in xrange(len(lawn[k])):
            print lawn[k][l],
    print ""
    
def solve( N, M, yard ):
    rows = [ max(yard[i]) for i in xrange(N) ]
    cols = [ max( [yard[i][j] for i in range(N) ] ) for j in range(M) ]

    for i in xrange(N):
        for j in xrange(M):
            if yard[i][j] < min( rows[i], cols[j] ):
                return "NO"
    return "YES"
    

b = open(r"d:/downloads/B-large.in", "r")

ans = ""
count = int(b.readline())
for i in xrange(1,count+1):
    size = b.readline().split(' ')
    N = int(size[0])
    M = int(size[1])

    lawn = []
    for j in xrange(N):
        tmp = map( lambda x: int(x), b.readline().split())
        lawn += [tmp]
        
    ans += "Case #%d: %s\n" % ( i, solve(N,M,lawn))
    
b.close()
bout = open(r"d:/downloads/b.out", "w")
bout.write(ans.strip())
print ans.strip()
bout.close()
