def mininbh(i,j,m):
    nbs=[]
    if i-1>=0:
        nbs.append([[i-1,j],m[i-1][j]])
    else: 
        nbs.append([[i-1,j],10000])
    if j-1>=0:
        nbs.append([[i,j-1],m[i][j-1]])
    else: 
        nbs.append([[i,j-1],10000])
    try: nbs.append([[i,j+1],m[i][j+1]])
    except: nbs.append([[i,j+1],10000])
    try: nbs.append([[i+1,j],m[i+1][j]])
    except: nbs.append([[i+1,j],10000])               
    return min(nbs,key=lambda x: x[1])

cases=int(raw_input())
for x in xrange(cases):
    m=[]
    m0=[]
    h,w=map(int, raw_input().split())
    for y in xrange(h):
        tmp=map(int, raw_input().split())
        m.append(tmp[:])
        m0.append(tmp)
    sinks=[]
    for i in xrange(h):
        for j in xrange(w):
            cur=m[i][j]
            mini=mininbh(i,j,m)
            if mini[1]>=cur:
                sinks.append([i,j])
    for i in xrange(h):
        for j in xrange(w):
            ci=i
            cj=j
            while True:
                cur=m[ci][cj]
                mini=mininbh(ci,cj,m)
                if mini[1]<cur:
                    ci=mini[0][0]
                    cj=mini[0][1]
                else:
                    m0[i][j]=sinks.index([ci,cj])
                    break
    out=""
    letters={}
    lp=ord('a')
    for i in xrange(h):
        for j in xrange(w):
            cp=m0[i][j]
            if cp in letters:
                out+="%s "%letters[cp]
            else:
                letters[cp]=chr(lp)
                out+="%s "%letters[cp]
                lp+=1
        out=out.rstrip()+"\n"
    print "Case #%i:"%(x+1)
    print out.rstrip()
            

