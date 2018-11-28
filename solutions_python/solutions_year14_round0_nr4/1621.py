import sys

T = int(sys.stdin.readline())

def dwar(nd, kd):
    cnt = 0
    l = len(kd)
    for i in range(l):
        k = kd[0]
        del kd[0]
        if nd[0] > k:
            del nd[0]
            cnt += 1
            continue
        else:
            n = nd.pop()
    return cnt

def war(nd, kd):
    cnt = 0
    l = len(kd)
    for i in range(l):
        n = nd[0]
        del nd[0]

        index, k = -1, -1
        for i in range(len(kd)-1, -1, -1):
            if kd[i] > n:
                index = i
                break
        k = kd[index]
        del kd[index]

        if k > n:
            cnt += 1
    return l - cnt

for k in range(1, T+1):
    sys.stdin.readline()
    nd = [float(i) for i in sys.stdin.readline().split()]
    kd = [float(i) for i in sys.stdin.readline().split()]
    nd = sorted(nd, reverse=True)
    kd = sorted(kd, reverse=True)

    ndd,kdd = nd[:],kd[:]
    num1 = dwar(nd, kd)
    num2 = war(ndd, kdd)

    print 'Case #%d: %d %d' % (k, num1, num2)
