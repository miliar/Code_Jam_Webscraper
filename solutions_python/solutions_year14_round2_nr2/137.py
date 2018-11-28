f=open('input','r')
t=int(f.readline())
for case in xrange(1,t+1):
    a,b,k=(int(e) for e in f.readline().split())
    count=0
    for i in xrange(0,a):
        for j in xrange(0,b):
            if i&j <k:
                count+=1
    print 'Case #%d: %d'%(case,count)
