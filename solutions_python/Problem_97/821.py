T = int(raw_input())

def getdigits(n) :
    res = []
    while n > 0 :
        dig = n % 10
        res.append(dig)
        n = n / 10
    res.reverse()
    return res

def getnumwithoffset(dig, offset) :
    n = 0
    L = len(dig)
    for i in range(L) :
        n *= 10
        n += dig[((i + offset) % L)]
    return n

for case in range(T) :
    A, B = [int(i) for i in raw_input().split(' ')]
    count = 0
    pairs = []
    for n in range(A, B+1) :
        d = getdigits(n)
        for h in range(len(d)) :
            f = getnumwithoffset(d, h)
            if len(str(f)) == len(str(n)) and f > n and f <= B :
                if not (n, f) in pairs :
                    count +=1
                    pairs.append((n, f))
    print "Case #%d:" % (case+1), count
        
        
