def findMax(num, k):
    pt = 0
    ind = 0
    for i in xrange(num):
        pt += 2**i
        if k <= pt:
            ind = i
            break
    # ind+1 for use
    if num-k+1 <= 2**ind:
        return 0
    if (num-k+1-2**ind)%(2**(ind+1)) == 0:
        return (num-k+1-2**ind)/2**(ind+1)
    return (num-k+1-2**ind)/2**(ind+1)+1

def findMin(num, k):
    pt = 0
    ind = 0
    for i in xrange(num):
        pt += 2**i
        if k <= pt:
            ind = i
            break
    # ind+1 for use
    return (num-k)/2**(ind+1)

t = int(raw_input())
for i in xrange(t):
    n, k = [int(s) for s in raw_input().split(" ")]
    print "Case #{}: {} {}".format(i + 1, findMax(n, k), findMin(n, k))
