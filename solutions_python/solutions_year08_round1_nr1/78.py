


numCasos=int(raw_input())

for caso in xrange(1, numCasos+1) :
    dim = int(raw_input())
    v1=[]
    v2=[]
    #leer vector 1
    
    for comp in raw_input().split() :
        v1.append(int(comp))

    for comp in raw_input().split() :
        v2.append(int(comp))

    v1.sort()
    v2.sort(reverse=True)

    total=0
    for i in xrange(dim):
        total += v1[i]*v2[i]

    print "Case #%d: %d"%(caso,total)
