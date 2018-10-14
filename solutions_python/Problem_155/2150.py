with open('A.0.large') as f:
    ncases = int(f.readline());
    for i in range(ncases):
        rawcase = f.readline().split()
        smax = int(rawcase[0])
        audience = rawcase[1]
        maxl = 0
        res = 0
        for s, n in enumerate(audience):
            n = int(n)
            if n == 0:
                if maxl > 0:
                    maxl -= 1
                else:
                    res += 1
            else:
                maxl += n - 1

        print "Case #{}: {}".format(i + 1, res)