from Queue import PriorityQueue
def pkts(n,u):
    # 0.9ku <= n <= 1.1ku => (10*n+11*u-1)/(11*u) <= k <= (10*n)/(9*u)
    return ((10*n+11*u-1)/(11*u),(10*n)/(9*u))

t = input()
for icase in range(1,t+1):
    n,p = map(int,raw_input().split())
    r = map(int,raw_input().split())
    q = []
    for i in range(n):
        row = [pkts(x,r[i]) for x in map(int,raw_input().split())]
        row.sort(None,None,True)
        q.append(row)
    res = 0
    pool = PriorityQueue(n)
    vmx,imx = (-1,-1),0
    for i,it in enumerate(q):
        pool.put((it[-1], i))
        vmx,imx = max((vmx,imx), (it[-1],i))
        it.pop()
    done = False
    while not done:
        assert not pool.empty()
        vmn,imn = pool.get()
        if max(vmn[0],vmx[0]) > min(vmn[1],vmx[1]):
            #print 'Drop!'
            if len(q[imn]) == 0:
                done = True
                break
            vmn = q[imn][-1]
            q[imn].pop()
            assert not pool.full()
            pool.put((vmn,imn))
            vmx,imx = max((vmx,imx), (vmn,imn))
        else:
            #print 'Serv!'
            if min(vmn[1],vmx[1]) > 0:
                res += 1
            pool = PriorityQueue(n)
            vmx,imx = (-1,-1),0
            for i,it in enumerate(q):
                if len(it) == 0:
                    done = True
                    break
                assert not pool.full()
                pool.put((it[-1], i))
                vmx,imx = max((vmx,imx), (it[-1],i))
                it.pop()
    print 'Case #%d: %d' % (icase, res)