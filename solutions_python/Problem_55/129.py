debug=False
def xl(l):
    return xrange(len(l))

def next(l):
    s=0
    for i in xl(l):
        s+=l[i]
        if s>k: return (i,s-l[i])
    return (len(l),s)

for case in range(input()):
    print "Case #"+str(case+1)+":",
    R,k,N=map(int,raw_input().split())
    g=map(int,raw_input().split())
    #print R,k,N
    #print g
    nx=[next(g[i:]+g[:i]) for i in xl(g)]
    cur=0
    loop=[]
    total=0
    totals=[0]
    while cur not in loop:
        loop.append(cur)
        total+=nx[cur][1]
        totals.append(total)
        cur=(cur+nx[cur][0])%len(g)
    startpart=loop[:loop.index(cur)]
    if R<=len(startpart):
        startval=totals[R%len(startpart)]
        R=0
    else:
        startval=totals[len(startpart)]
        R=R-len(startpart)
        totals=[x-totals[len(startpart)] for x in totals[loop.index(cur):]]
    loop=loop[loop.index(cur):]
    print startval+R/len(loop)*totals[-1]+totals[R%len(loop)]
    if debug:
        print totals
        print nx
        print startpart
        print loop
        print total
