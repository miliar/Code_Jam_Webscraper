import math

def getcost2 (es,qs):
        oks=[]
        for e in es:
                i=0
                for q in qs:
                        if q == e:
                                break
                        i=i+1
		oks.append(i)
	return oks

def getcost (es,qs):
        c=0
        i=0
        while len(qs) > 0:
                i = sorted(getcost2(es,qs),reverse=True)[0]
                qs=qs[i:]
                if len(qs) > 0:
                        c=c+1
	return c

fd = open ("As.in", "r")
#fd = open ("input.txt", "r")

n=int(fd.readline())
for i in range (1,n+1):
        s=int(fd.readline())
        engines=[]
        for j in range(0,s):
                engines.append (fd.readline().strip('\n'))
	q=int(fd.readline())
	queries=[]
	for j in range(0,q):
                queries.append (fd.readline().strip('\n'))
        print "Case #" + str(i) + ": " + str(getcost (engines,queries))
