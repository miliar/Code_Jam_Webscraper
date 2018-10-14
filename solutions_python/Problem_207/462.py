
from math import ceil

class Breed:
    def __init__(self, c, n):
        self.c = c
        self.n = n

def arrange(n, r, o, y, g, b, v):
    l = [' ']*n
    uni = [Breed('R', r), Breed('Y', y), Breed('B', b)]
    uni.sort(key = lambda x: x.n, reverse = True)
    if n < 2*uni[0].n:
        return 'IMPOSSIBLE'
    k = uni[0].n
    c = uni[0].c
    interval = float(n) / float(k)
    ind = 0
    while k > 0:
        interval = int(ceil(float(n-ind) / float(k)))
        l[ind] = c
        ind2 = 1 if uni[1].n >= uni[2].n else 2
        for j in range(ind+1, ind+interval):
            if uni[ind2].n == 0:
                return 'IMPOSSIBLE'
            l[j] = uni[ind2].c
            uni[ind2].n -= 1
            ind2 = 2 if ind2 == 1 else 1
        #print "'" + ''.join(l) + "'"
        ind += interval
        k -= 1
    
    
    return ''.join(l)
    
            


t = int(raw_input())
for i in xrange(1, t + 1):
    line = raw_input()
    (n, r, o, y, g, b, v) = map(lambda x: int(x), line.split(' '))
    print "Case #{}: {}".format(i, arrange(n, r, o, y, g, b, v))
