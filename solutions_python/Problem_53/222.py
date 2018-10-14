import sys
import math

def run(N, K):
    if K == 0:
        return 0
    m = 2**N - 1
    if (K & m) == m:
        return 1
    else:
        return 0
    

def main(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    T = int(lines[0])
    for i in range(1, T+1):
        N, K = lines[i].split()
        N = int(N)
        K = int(K)
        res = run(N, K)
        if res:
            res = 'ON'
        else:
            res = 'OFF'
        print "Case #%d: %s" % (i, res)

if __name__ == '__main__':
    main(sys.argv[1])