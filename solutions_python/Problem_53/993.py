def solve(N, K):
    N = int (N)
    K = int (K)
    NN = 2 ** N
    while K > NN :
        K = K - NN
    if K == (NN - 1):
        return 'ON'
    else:
        return 'OFF'

def main(fn):
    fi = open(fn, 'r')
    fo = open(fn + 'out', 'w')
    line = fi.readline()
    n = 0
    while line:
        n = n + 1
        line = fi.readline()
        nk = line.split()
        if len(nk) is 2:
            wl = 'Case #%s: %s' % (n ,solve(*nk))
            fo.write(wl + '\n')
    fi.close()
    fo.close()
