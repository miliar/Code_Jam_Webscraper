import sys
T=int(sys.stdin.readline())
for a in range(T):
    main=list(sys.stdin.readline().split("/"))
    N=int(main[0])
    D=int(main[1])
    count=1
    while True:
        K=float(D)/2
        if K-round(K)!=0:
            print "Case #" + str(a+1) + ": " + "impossible"
            break
        if K<N:
            while True and K!=1:
                q=K/2
                if q-round(q)!=0:
                    count="impossible"
                    break
                K=K/2
            print "Case #" + str(a+1) + ": " + str(count)
            break
        if K==N:
            print "Case #" + str(a+1) + ": " + str(count)
            break
        D=D/2
        count+=1