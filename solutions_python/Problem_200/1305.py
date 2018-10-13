t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n = int(raw_input())
    
    l = map(int, list(str(n)))
    res = n
    if len(l) != 1:
        cut = -1
        for j in range(1, len(l)):
            if l[j] < l[j-1]:
                cut = j
        
        if cut != -1:
            for j in range(cut, len(l)):
                l[j] = 9
            l[cut-1] -= 1

            for j in range(cut-1, 0, -1):
                if l[j] < l[j-1]:
                    for k in range(j, len(l)):
                        l[k] = 9
                    l[j-1] -= 1
            
            res = int(''.join(map(str, l)))

    print "Case #{}: {}".format(i, res)

