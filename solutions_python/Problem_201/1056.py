import math

"""def level(stalls, k):
    res = 1
    while 2**res < k:
        stalls = int(stalls / 2)
        res += 1
    return res
"""
def lr(stalls, k):
    if stalls == 1:
        return (0,0)
    if stalls == 2 and k == 1:
        return (1,0)
    elif stalls == 2:
        return (0,0)
    elif stalls == k:
        return (0,0)
    #l = level(stalls, k)
    l = int(math.log(k,2))
    rest = stalls - 2**l + 1
    r = rest % (2**l)
    d = rest / (2**l)
    # r x d+1, 2**l - r ma d
    tst = k - 2**l + 1
    if tst <= r:
        slot = d + 1
    else:
        slot = d
    l, r = int(math.ceil((slot - 1) / 2.)), int(math.floor((slot - 1) / 2.))
    return (l,r)

if __name__ == "__main__":
    
    f = open("input.txt")
    lines = f.readlines()
    f.close()
    t = int(lines[0].strip() )
    i = 1
    while i <= t:
        n, k = map(int, lines[i].strip().split(' '))
        l,r = lr(n,k)
        print "Case #%d: %d %d" % (i, l, r)
        i += 1    


