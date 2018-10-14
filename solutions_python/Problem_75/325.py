import sys
fi=open('B-large.in')
sys.stdout=open("B-large.out","w")
T=int(fi.readline())
for tn in range(T):
    l=fi.readline().split()
    N=int(l[0])
    comps=l[1:N+1]
    C=int(l[N+1])
    oppsr=l[N+2:C+N+2]
    comps=dict([(c[:2],c[-1]) for c in comps]+[(c[1]+c[0],c[-1]) for c in comps])
    opps={}
    for o in oppsr:
        opps[o[0]]=opps.get(o[0],set()) | set([o[1]])
        opps[o[1]]=opps.get(o[1],set()) | set([o[0]])
    l=l[-1]
    
    r='0'
    clearif=set()
    clearifold=set()
    for i,c in enumerate(l):
        r+=c
        if r[-2:] in comps:
            r=r[:-2]+comps[r[-2:]]
            clearif=clearifold
        elif c in clearif:
            r='0'
            clearif.clear()
            clearifold.clear()
        else:
            clearifold=clearif
            if c in opps:
                clearif=clearif | opps[c]
    print "Case #%d: [%s]"%(tn+1,", ".join(r[1:]))
fi.close()