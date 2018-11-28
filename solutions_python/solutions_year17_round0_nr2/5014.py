t = int(raw_input())
for i in xrange(1, t + 1):
    n = int(raw_input())
    for k in range(n):
        m = str(n-k)
        lst = []
        c = 0
        for j in m:
            lst.append(int(j))
        for l in range(len(lst) - 1):
            if lst[l] > lst[l+1]:
                c = 1
                break
        if c == 0:
            break
                

    print "Case #{}: {}".format(i,m)
 
