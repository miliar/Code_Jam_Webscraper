t = int(raw_input())

for i in xrange(1, t + 1):
    a = [int(c) for c in raw_input()]

    for j in xrange(len(a)-1, 0, -1):
        if (a[j] < a[j-1]):
            a[j-1]-=1
            for k in xrange(j, len(a)):
                a[k]=9
    
    result = long(''.join(map(str,a)))
    print "Case #{}: {}".format(i, result)
