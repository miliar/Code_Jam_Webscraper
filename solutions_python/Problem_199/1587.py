def flip(cakes, k):
    flips = 0

    for i in range(len(cakes) - k + 1):
        if cakes[i] == '-':
            flips += 1
            for j in range(k):
                if cakes[i + j] == '-':
                    cakes[i + j] = '+'
                else:
                    cakes[i + j] = '-'
    
    if ''.join(cakes[-k+1:]) == '+' * (k-1):
        return flips
    
    return 'IMPOSSIBLE'

tc = int(raw_input())

for t in xrange(1, tc + 1):
    cakes, k = raw_input().split(' ')
    res = flip(list(cakes), int(k))
    print "Case #{}: {}".format(t, res)