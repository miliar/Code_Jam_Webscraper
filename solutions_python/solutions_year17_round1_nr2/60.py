import math
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    N, P = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    Rs = [int(s) for s in raw_input().split(' ')]
    Qs = []
    for j in range(N):
        Qs.append([int(s) for s in raw_input().split()]) 

    # print N, P
    # print Rs
    # print Qs

    counts = []
    kits = []

    for j in range(N):
        qs = Qs[j]
        r = Rs[j]
        ks = []
        for k, q in enumerate(qs):
            m = int(math.ceil((float(q) / 1.1) / r))
            M = int(math.floor((float(q) / 0.9)/ r))
            
            if m <= M:
                ks.append([m,M])
            else:
                ks.append([0,0])

        ks = sorted(ks, key=lambda a:(-a[1], -a[0]))
        kits.append(ks)
    
    # if i == 90:
        # print kits


    cnt = 0
    for k in range(P):
        rg = kits[0][k]
        if rg == [0,0]: continue
        use_k = []
        failed = False
        # print rg
        for p in range(1, len(kits)):
            ks = kits[p]
            found = False
            for a, rg_1 in enumerate(ks):
                # print 'rg1', rg_1
                if rg[0] <= rg_1[1] and rg_1[0] <= rg[1]:
                    # print 'yo'
                    rg[0] = max(rg[0], rg_1[0])
                    rg[1] = min(rg[1], rg_1[1])
                    use_k.append(a)
                    found = True
                    break
            if not found:
                failed = True
                break
        
        if not failed:
            cnt += 1
            for p,k in enumerate(use_k):
                del kits[p+1][k]
    

    print "Case #{}: {}".format(i, cnt)

