import collections

ri = lambda : raw_input().strip()
rim = lambda tp, deli: map(tp, ri().split(deli))

n = int(ri())

for i in xrange(n):
    A, B, K = rim(int, ' ')
    result = 0
    
    for x in xrange(A):
        for y in xrange(B):
            val = x & y
            
            if val < K:
                result += 1
    
    print "Case #{}: {}".format(i+1, result)
    