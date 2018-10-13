
def divide(n, k):
    #print "divide(%d, %d)" % (n, k)
    if n % 2 == 0:
        l = n/2 - 1
        r = n/2
    else:
        l = (n-1)/2
        r = (n-1)/2
    
    if k == 1:
        return [l,r]
    if k == 2:
        return divide(r, 1)
    
    if l == r:
        if (k-1) % 2 == 0:
            return divide(r, (k-1)/2)
        else:
            return divide(l, (k-2)/2 + 1)
    else:
        if (k-1) % 2 == 0:
            return divide(l, (k-1)/2)
        else:
            return divide(r, (k-2)/2 + 1)
                


t = int(raw_input())
for i in xrange(1, t + 1):
    n, k = [int(s) for s in raw_input().split(" ")]
    rv = divide(n, k)
    rv.sort()
    print "Case #{}: {} {}".format(i, rv[1], rv[0])
