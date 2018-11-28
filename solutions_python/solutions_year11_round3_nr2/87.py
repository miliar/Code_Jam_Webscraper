import sys, itertools

f = open(sys.argv[1])
fout = open(sys.argv[2], "w")

rl = lambda: f.readline().strip()
ra = lambda type: map(type, rl().split())
ri = lambda: int(rl())

T = ri()
for tt in xrange(T):
    d = ra(int)
    (L, t, N, C), cc = d[:4], d[4:]
    
    timeN = 2*sum(cc)*(N/C) + 2*sum(cc[:N%C])
    if t >= timeN:
        r = timeN
    else:
        d = 0
        n = 0
        csum = sum(cc)
        
        # skip C before t
        while d+2*csum <= t: # and n+C <= N:
            d += 2*csum
            n += C
       
        # skip before t
        for i, x in enumerate(cc):
            if d+2*x > t: # or n+1 > N:
                break
            d += 2*x
            n += 1
       
        # skip on t
        boosts = [(d+2*x - t) / 2]
        d += 2*x
        n += 1

        # skip after t
        for x in cc[i+1:]:
            if n >= N: 
                break
            d += 2*x
            n += 1
            boosts += [x]

        # skip C after t
        while n+C <= N:
            d += 2*csum
            n += C
            boosts += cc

        # skip rest
        if n < N:
            d += 2*sum(cc[:N-n])
            n = N
            boosts += cc[:N-n]
       
        boosts.sort(reverse=True)
       
        r = d - sum(boosts[:L])


    print >>fout, "Case #%d: %d" % (tt+1, r)
       