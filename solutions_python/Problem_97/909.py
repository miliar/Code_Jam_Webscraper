f = open('C-small-attempt0.in')
oo = open('C.out','w')

T = int(f.readline())
for cas in range(T):
    data = f.readline().split()
    A = int(data[0])
    B = int(data[1])
    tot = 0
    for i in range(A,B):
        Si = str(i)
        Li = len(Si)
        L = []
        for j in range(1,Li):
            St = Si[Li-j:]+Si[:Li-j]
            ii = int(St)
            if (ii>i and ii<=B and ii not in L):
                #print i,ii
                tot += 1
                L.append(ii)
    oo.write("Case #"+str(cas+1)+": "+str(tot)+'\n')

f.close()
oo.close()
