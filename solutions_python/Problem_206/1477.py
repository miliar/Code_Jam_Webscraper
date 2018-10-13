data = open('A-large.in','r')
d = open('ans1.out','w')

cases = int(data.readline())

for x in range(cases):
    di,hn = map(int,data.readline().split())
    t = 0;t2 = 0;pt = 0
    for i in range(hn):
        p,s = map(float,data.readline().split())
        pt = (di-p)/s
        if pt > t:
            t = pt;dis = p
    ans = di/(t)

    print >>d,'Case #{}: {}'.format(x+1,"{0:.6f}".format(ans))
        
d.close()
