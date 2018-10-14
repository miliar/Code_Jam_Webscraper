import sys, linecache

filename=sys.argv[1]
cn=int(linecache.getline(filename,1))

def compp(aa,bb):
    cc=sorted(aa)
    dd=sorted(bb)
    aa=sorted(aa,reverse=True)
    bb=sorted(bb,reverse=True)
    #print aa
    #print bb
    #print cc
    #print dd
    c=0
    d=0
    i=0
    j=0
    while i<=len(aa)-1 and j<=len(bb)-1:
     #   print i,j
        if aa[i]>bb[j]:
            c=c+1
            i=i+1
            j=j+1
        else:
            j=j+1
    i=0
    j=0
    while i<=len(cc)-1 and j<=len(cc)-1:
        if dd[i]>cc[j]:
            d=d+1
            i=i+1
            j=j+1
        else:
            i=i+1
    d=len(aa)-d
    return c,d

for i in range(cn):
    count=int(linecache.getline(filename,i*3+2))
    nami=linecache.getline(filename,3*i+3).strip('\n').split(' ')
    ken=linecache.getline(filename, 3*i+4).strip('\n').split(' ')
    nami_f=[float(aa) for aa in nami]
    ken_f=[float(bb) for bb in ken]
    c,d=compp(nami_f,ken_f)
    print "Case #%s: %s %s" %(i+1,c,d)
