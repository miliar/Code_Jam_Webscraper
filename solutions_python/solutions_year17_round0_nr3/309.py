def stall(n, p):
    d = {n: 1}

    level = 0

    while 2**level < p:
        # split a level
        new_d = {}
        for k,v in d.iteritems():
            if k % 2 == 1:
                if k/2 not in new_d: new_d[k/2] = 0
                new_d[k/2] += d[k]*2

            else:
                if k/2 not in new_d: new_d[k/2] = 0
                if k/2-1 not in new_d: new_d[k/2-1] = 0
                new_d[k/2] += d[k]
                new_d[k/2-1] += d[k]

        d = new_d

        p -= 2**level
        level += 1

        

    if p == 0:
        keys = d.keys()
        k = min(keys)
        if k % 2 == 1:
            # Odd
            return k, k 
        else:
            # Even
            return k / 2, max(k / 2 - 1, 0)

    else:
        
        keys = d.keys()
        max_k = max(keys)
        min_k = min(keys)
        if d[max_k] >= p:
            k = max_k
        else:
            k = min_k



        if k % 2 == 1:
            # Odd
            return k / 2, k / 2
        else:
            # Even
            return k / 2, max(k / 2 - 1, 0)



for i in xrange(input()):
    n, p = map(int, raw_input().split(" "))
    mn, mx = stall(n, p) 
    print "Case #%d: %d %d" % ((i+1), mn, mx)
