def prog():
    n,m = map(int,raw_input().split())
    inp = []
    dp = []
    for _ in xrange(n):
        inp += [list(raw_input())]
    mr = [0]*n
    for i in xrange(n):
        for j in xrange(m-2,-1,-1):
            if(inp[i][j]=='?' and inp[i][j+1]!='?'):
                inp[i][j]=inp[i][j+1]
        for j in xrange(1,m):
            if(inp[i][j]=='?' and inp[i][j-1]!='?'):
                inp[i][j]=inp[i][j-1]
        if(inp[i].count('?') == m):
            mr[i] = -1
        else:
            mr[i] = i
    for i in xrange(n-2,-1,-1):
        if(mr[i]==-1 and mr[i+1]!=-1):
            mr[i]=mr[i+1]
    for i in xrange(1,n):
        if(mr[i]==-1 and mr[i-1]!=-1):
            mr[i]=mr[i-1]
    for i in xrange(n):
        for j in xrange(m):
            inp[i][j]=inp[mr[i]][j]
    for i in inp:
        print "".join(i)
                    
t = input()
for T in xrange(1,t+1):
    print "Case #"+str(T)+":"
    prog()
