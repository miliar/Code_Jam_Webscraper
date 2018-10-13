dirs=[(-1,0),(0,-1),(0,1),(1,0)]
def addv(v1,v2):
    return (v1[0]+v2[0],v1[1]+v2[1])

def ingrid(v):
    return v[0]>=0 and v[1]>=0 and v[0]<h and v[1]<w

for t in xrange(input()):
    h,w=map(int,raw_input().split())
    alt=[]
    for i in xrange(h):
        alt.append(map(int,raw_input().split()))
    children=[[[] for i in xrange(w)] for j in xrange(h)]
    sinks=[]
    for i in xrange(h):
        for j in xrange(w):
            m=alt[i][j]
            low=(i,j)
            for d in dirs:
                p=addv((i,j),d)
                if ingrid(p) and alt[p[0]][p[1]]<m:
                    m=alt[p[0]][p[1]]
                    low=p
            if low==(i,j):
                sinks.append((i,j))
            else:
                children[low[0]][low[1]].append((i,j))
    
    bassins=[]
    for s in sinks:
        q=[s]
        b=[]
        while 1:
            if len(q)==0: break
            q+=[c for c in children[q[0][0]][q[0][1]] if c not in b]
            b.append(q.pop(0))
        bassins.append(b)
    bassins.sort(key=lambda x: min(x))
    mapout=[["" for i in xrange(w)] for j in xrange(h)]
    c=97
    for b in bassins:
        for p in b:
            mapout[p[0]][p[1]]=chr(c)
        c+=1
    print "Case #"+str(t+1)+":"
    for r in mapout:
        for c in r:
            print c,
        print
