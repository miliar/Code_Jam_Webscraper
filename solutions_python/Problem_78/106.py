
f = open('A-large.in','r')
T = int(f.readline().strip())

for ti in xrange(1,T+1):
    n,pd,pg = map(int,f.readline().split())
    #print n,pd,pg
    s = 'Broken'
    if pd==0 and pg==0: s = 'Possible'
    elif pd==0 and pg!=0: s = 'Broken'
    elif pg==0 and pd!=0: s = 'Broken'
    elif pg==100 and pd==100: s = 'Possible'
    elif pg==100 and pd!=100: s = 'Broken'
    else:
        for di in xrange(1,n+1):
            if (pd*di)%100==0:
                s = 'Possible'
                break
    print 'Case #%d: %s'%(ti,s)
