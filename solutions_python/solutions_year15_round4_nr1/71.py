for t in xrange(input()):
    R,C = map(int,raw_input().split())
    m = [raw_input().strip() for _ in xrange(R)]
    r = [(min([C]+[i for i in xrange(C) if m[j][i]!='.']),max([-1]+[i for i in xrange(C) if m[j][i]!='.'])) for j in xrange(R)]
    c = [(min([R]+[i for i in xrange(R) if m[i][j]!='.']),max([-1]+[i for i in xrange(R) if m[i][j]!='.'])) for j in xrange(C)]
    fail = retval = 0
    for i in xrange(R):
        if fail: break
        for j in xrange(C):
            if fail: break
            d = m[i][j]
            if d=='<':
                if r[i][0]==j and r[i][1]==j and c[j][0]==i and c[j][1]==i: fail = 1
                elif r[i][0]>=j: retval+=1
            elif d=='>':
                if r[i][0]==j and r[i][1]==j and c[j][0]==i and c[j][1]==i: fail = 1
                elif r[i][1]<=j: retval+=1
            elif d=='^':
                if r[i][0]==j and r[i][1]==j and c[j][0]==i and c[j][1]==i: fail = 1
                elif c[j][0]>=i: retval+=1
            elif d=='v':
                if r[i][0]==j and r[i][1]==j and c[j][0]==i and c[j][1]==i: fail = 1
                elif c[j][1]<=i: retval+=1
    if fail: retval = 'IMPOSSIBLE'
    print "Case #%d: %s"%(t+1,retval)
