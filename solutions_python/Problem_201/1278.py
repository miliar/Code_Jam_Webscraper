import sys, math

def printResult(i, smax, smin) :
    print('Case #{0}: {1} {2}'.format(i, smax, smin))

t = int(sys.stdin.readline())
for i in range(1, t + 1):
    nk = sys.stdin.readline().split(' ')
    n = int(nk[0])
    k = int(nk[1])

    klog2 = int(math.log2(k))
    maxinkrank = (2 ** (klog2 + 1)) - 1
    base = (n - maxinkrank) // (2 ** (klog2 + 1))
    remain = (n - maxinkrank) % (2 ** (klog2 + 1))
    if remain > (k - (2 ** klog2)):
        smax = base + 1
    else:
        smax = base
    if remain > k:
        smin = base + 1
    else:
        smin = base

    printResult(i, smax, smin)
