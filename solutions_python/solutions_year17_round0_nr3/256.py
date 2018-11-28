def fun(N, K):
    if K == 1:
        return "{0} {1}".format(N/2, (N-1)/2)
    pow = 1
    K -= 1
    high, low = N/2, (N-1)/2
    highCount, lowCount = 1, 1
    while K > 2*pow:
        K -= 2*pow
        pow *= 2
        if high == low:
            highCount, lowCount = highCount + lowCount, highCount + lowCount
        elif high % 2 == 1:
            highCount, lowCount = highCount*2 + lowCount, lowCount
        else:
            highCount, lowCount = highCount, highCount + lowCount*2
        high, low = high / 2, (low-1) / 2
#        print [K, pow, high, low, highCount, lowCount]
    if K <= highCount:
        return "{0} {1}".format(high/2, (high-1)/2)
    else:
        return "{0} {1}".format(low/2, (low-1)/2)

n = int(raw_input())
for i in range(n):
    input = map(int, raw_input().strip().split(' '))
    print "Case #{0}: {1}".format(i+1, fun(input[0], input[1]))
