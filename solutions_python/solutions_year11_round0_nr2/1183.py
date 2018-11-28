s=open('B.in').read()
out=open('B.out','w')
a=s.split('\n')[1:]
for ia in xrange(len(a)):
    if not a[ia]: continue
    d=a[ia].split()
    nc=int(d[0])
    ct = d[1:nc+1]
    c=[]
    for i in ct:
        c.append(i)
        c.append(i[1]+i[0]+i[2])
    no = int(d[nc+1])
    ot = d[nc+2:nc+no+2]
    o=list()
    for i in ot:
        o.append(i)
        o.append(i[1]+i[0])    
    l=list(d[-1])
    h=list()
    h.append(l[0])
    for j in l[1:]:
        'print j,h'
        for co in c:
            if h:
                if h[-1]==co[0] and j==co[1]:
                    h[-1]=co[2]
                    break
        else:
            for oo in o:
                if(oo[0]==j and oo[1] in h):
                    h=[]
                    break
            else:
                h.append(j)
    out.write('Case #{0}: '.format(ia+1)+str(h).replace('\'','')+'\n')
out.close()
            
