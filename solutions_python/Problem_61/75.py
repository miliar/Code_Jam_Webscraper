def is_pure(n, subset):
    while True:
        if n in subset:
            n = subset.index(n)+1
            if n == 1:
                return 1
        else:
            return 0 
ys = {}    
T = int(raw_input())
for t in range(T):
    n = int(raw_input())
    if n in ys:
        y = ys[n]
    else:
        y = 0
        subsets = []
        twoton = range(2, n)
        for i in range(2**(n-2)):
            s = []
            for j in range(n-2):
                if (i >> j & 1):
                    s.append(twoton[j])
            s.append(n)
            subsets.append(s)
        y = sum(map(lambda x: is_pure(n, x), subsets))
        ys[n] =y
    
    print 'Case #%d: %d' % (t+1, y%100003)

            


    