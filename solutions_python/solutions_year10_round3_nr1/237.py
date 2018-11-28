f=open('A-large.in')
g=open('A-large.out','w')
T=int(f.readline())
for t in range(1,T+1):
    N=int(f.readline().strip())
    AB=[]
    for n in range(N):
        a,b = [int(s) for s in f.readline().strip().split()]
        AB.append([a,b])
    intersections=0
    for this in AB:
        this_crosses = [((this[0]<ab[0] and this[1]>ab[1]) or (this[0]>ab[0] and this[1]<ab[1])) for ab in AB]
        intersections = intersections + sum(this_crosses)
    intersections = intersections/2
    print >>g, "Case #"+str(t)+": "+str(intersections)

f.close()
g.close()

print 'done!'
