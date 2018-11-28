fin = open('C-small-attempt2.in')
fo = open('C.out','w')
t = int(fin.readline())

def fill_it(k,g,i,n):
    l = g[i]
    i+=1
    for c in xrange(1,n):
        if i == n:
            i = 0
        if l+g[i] > k:
            break
        l+=g[i]
        i+=1
    if i == n:
        i = 0
    return (l,i)

for j in xrange(1,t+1):
    r,k,n = [int(x) for x in fin.readline().split()]
    g = [int(x) for x in fin.readline().split()]
    
    i = 0
    h = {}
    cost = 0
    for rr in xrange(0,r):
        if i in h:
            cost+=h[i][0]
            i = h[i][1]
        else:
            (c,ni) = fill_it(k,g,i,n)
            h[i] = (c,ni)
            cost+=c
            i = ni
    
    fo.write("Case #{0}: {1}\n".format(j,cost))
print "Done"