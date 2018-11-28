f = open('D-large.in', 'r')
num = int(f.readline())
for x in range(0, num):
    num = f.readline()
    N = [float(z) for z in f.readline().split()]
    N.sort()
    K = [float(z) for z in f.readline().split()]
    K2 = list(K)
    Npoints = 0
    NDpoints = 0
    Kblock = 1.0
    for n in N:
        for k in K:
            if float(k)>float(n) and float(k)<Kblock:
                Kblock = k
        if(Kblock!=1.0):
            K.remove(Kblock)
            Kblock = 1.0
        else:
            K.remove(min(K))
            Npoints+=1
    for n in N:
        for k in K2:
            if float(n)>float(k):
                NDpoints+=1
                K2.remove(min(K2))
                break
    print "Case #" + str(x+1) + ": " + str(NDpoints), str(Npoints)
    
