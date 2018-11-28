for _ in range(int(input())):
    n,k = list(map(int, input().split()))
    n = n+2
    l = [0,n-1]
    sl = sorted(l)
    ki = k
    while ki>0:
        dif = -1
        iter = -1
        for i in range(len(sl)):
            if sl[i]-sl[i-1] > dif:
                dif = sl[i]-sl[i-1]
                iter = i-1
        l.append(sl[iter] + (dif//2))
        sl = sorted(l)
        ki = ki-1
    index = sl.index(l[-1])
    l = sl[index] - sl[index-1]-1
    r = sl[index+1] - sl[index]-1
    print("Case #"+str(_+1)+": "+str(max(l,r))+" "+str(min(l,r)))
