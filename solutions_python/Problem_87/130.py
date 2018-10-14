from collections import defaultdict



T = int(raw_input())


for case in range(T):
    X, S, R, T, N = map(int, raw_input().split())
    B = []
    E = []
    w = []

    dic = defaultdict(int)

    ans = 0.0

    onslopetime = 0.0
    for n in range(N):
        inb, ine, inw = map(int, raw_input().split())
        B.append(inb)
        E.append(ine)
        w.append(inw)
        #print ine-inb
        dic[S+inw] += float(ine-inb)
        onslopetime += float(ine-inb)
    #print X, S, R, T, N
    #print B
    #print E
    #print w
    dic[S] = X-onslopetime
    
    #print dic

    x = dic.items()
    x.sort()
    #print x
    for speed, length in x:
        fasttime = float(length) / (speed + (R-S))
        #print T

        if T == 0:
            ans += length / speed
        elif fasttime > T:
            restlength = length - (T * (speed + (R-S)))
            ans += T + restlength / speed
            T = 0
        else:
            ans += fasttime
            T -= fasttime
        #print speed, length, fasttime
    
    print "Case #%d: %f" % (case+1, ans)
