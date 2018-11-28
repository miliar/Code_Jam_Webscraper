from sys import argv

with open(argv[1]) as f:
    T = int(f.readline())
    for i in range(T):
        N = int(f.readline())
        ms = [int(j) for j in f.readline().split()]
        prec = ms[0]
        method1 = 0
        maxi = -1
        for m in ms[1:]:
            diff = max(prec - m, 0)
            if diff > maxi:
                maxi = diff
            method1 += diff
            prec = m
        method2 = 0
        prec = ms[0]
        for m in ms[1:]:
            inter = prec - maxi
            method2 += min(maxi, prec)
            prec = m
            
        print ("Case #"+str(i+1)+": "+str(method1)+" "+str(method2))
    
