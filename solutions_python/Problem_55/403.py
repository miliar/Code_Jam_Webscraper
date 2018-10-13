import sys
def run(R, K, N, G):
    sums = {}
    nxt =  {}
    D = []
    i = 0
    j = 0
    total = 0
    for r in range(R):
        s = 0
        if nxt.has_key(i):
            total += sums[i]
            i = nxt[i]
            j = i
        else:
            while s + G[j] <= K:
                s += G[j]
                j += 1
                j %= N
                if j == i:
                    break
            sums[i] = s
            nxt[i] = j
            total += s
            i = j
    return total

f = open(sys.argv[1])

for i,l in enumerate(f.readlines()):
    if i > 0 and len(l) > 1:
        if i & 1:
            R,K,N = l.split(' ')[0:3]
            R = int(R)
            K = int(K)
            N = int(N)
        else:
            G = [int(k) for k in l.split(' ')]
    if not i & 1 and i > 1:
        r = run(R,K,N,G)
        print 'Case #%s: %s' % (i/2,r)
