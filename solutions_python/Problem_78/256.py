inp=open('freecell.in')
T=int(inp.readline())
for caso in map(str,range(1,T+1)):
    cosas=map(int,inp.readline().strip().split(' '))
    n=cosas[0]
    pd=cosas[1]
    pg=cosas[2]
    if (pg==100 and pd<100) or (pg==0 and pd>0):
        print "Case #"+caso+": Broken"
        continue
    if pd==0 or pd==100:
        print "Case #"+caso+": Possible"
        continue

    listo=False
    for dg in range(n+1):
        if listo:break
        for d in range(max(1,dg),n+1):
            if (100*dg)/d==pd and (100*dg)%d==0:
                print "Case #"+caso+": Possible"
                listo=True
                break
    if not listo:
        print "Case #"+caso+": Broken"
