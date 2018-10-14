filename = "C:\\Users\\Andri_000\\Downloads\\python\\codejam2017\\Round 1C\\A\\A-large"

fin = open(filename+".in")
fout = open(filename+".out","w")
trials = int(fin.readline())



for T in xrange(trials):

    rh = []

    n, k = map(int, fin.readline().split(' ')) 
    for i in range(n):
        r, h = map(int, fin.readline().split(' '))
        rh.append((r, h))
        
    rh = sorted(rh, key = lambda x: -x[0])
    #print rh
    ans = 0
    
    for i in range(n-k+1):
        a = rh[i][0]**2 + 2*rh[i][0]*rh[i][1]
        arr = sorted(rh[i+1:], key = lambda x: -x[0]*x[1])
        #print arr
        a += 2*sum(map(lambda x: x[0]*x[1], arr[:k-1]))
        if a > ans:
            ans = a
        #print ans, a
    
    fout.write("Case #{0}: {1:.6f}\n".format(T+1, 3.14159265359*ans))
        
    print "Case #{0} done".format(T+1)
                    
fin.close()
fout.close()