f = open('B-small-attempt2.in','r')
fo = open('result.txt','w')
t = int(f.readline())
#  0N, 1R, 2O, 3Y, 4G, 5B, and 6V. 
d = [[],[2,6],[1,3],[2,4],[3,5],[4,6],[5,1]]
e = [[],[3,4,5],[4,5,6],[1,5,6],[1,2,6],[1,2,3],[2,3,4]]
st = 'XROYGBV'
for ti in range(t):
    u = [int(x) for x in f.readline().split()]
    #print(u)
    b = [[[],u]]
    soln = "IMPOSSIBLE"
    while b:
        h = b[0]
        b = b[1:]
        a = h[1]
        #print(len(b))
        if len(h[0]) == u[0]:
            if h[0][0] in e[h[0][-1]]:
                soln = ''.join(st[i] for i in h[0])
                break
        broken = False
        for i in range(1,7):
            if a[i]:
                s = 0
                for j in e[i]:
                    s += a[j]
                if s < a[i]-1:
                    broken = True
                    break
        if not broken:
            if h[0]:
                dl = e[h[0][-1]]
            else:
                dl = range(1,7)
            ji = max((a[j],j) for j in range(1,7) if j in dl)
            if ji[0] > 4:
                j = ji[1]
                a[j] -= 1
                b += [[h[0]+[j],a]]
            else:    
                for j in dl:
                    if a[j]:
                        a2 = a[:]
                        a2[j] -= 1
                        b += [[h[0]+[j],a2]]
    rs = "Case #%d: %s\n" % (ti+1, soln)
    #print(rs)
    fo.write( rs )
fo.close()
f.close()