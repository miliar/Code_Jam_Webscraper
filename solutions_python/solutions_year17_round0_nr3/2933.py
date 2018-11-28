t = int(raw_input())

def getLR(stalls, pos):
    l = 0
    r = 0
    while not stalls[pos-l-1]:
        l+=1
    while not stalls[pos+r+1]:
        r+=1
    return l, r

def c(a, b):
    if a[1] != b[1]:
        return a[1] - b[1]
    elif a[2] != b[2]:
        return a[2] - b[2]
    else:
        return b[0] - a[0]

def bestPos(stalls):
    options = []
    for i in range(1, len(stalls) - 1):
        if not stalls[i]:
            L, R = getLR(stalls, i)
            options.append((i, min(L, R), max(L, R)))
    return sorted(options, cmp=c)[-1][0]

for i in xrange(1, t + 1):
    n, k = [int(v) for v in raw_input().split(" ")]
  
    stalls = [True] + [False for _ in xrange(n)] + [True]

    for p in xrange(k-1):
        stalls[bestPos(stalls)] = True

    last = bestPos(stalls)
    L, R = getLR(stalls, last)
  
    print "Case #{}: {} {}".format(i, max(L, R), min(L, R))


