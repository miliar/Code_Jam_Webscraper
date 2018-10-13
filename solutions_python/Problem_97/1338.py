import math, sys
from multiprocessing import Pool

def main((A, B)):
    s = set()
    L = int(math.log10(B))
    log10 = [pow(10, i) for i in range(1, L+1)]
    for n in xrange(A, B+1):
        for l in log10:
            a = n / l
            b = n % l
            m = b * pow(10, int(math.log10(a)) + 1) + a
            if n < m <= B:
#                print n,m
                s.add((n,m))
    return str(len(s))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        f = open(sys.argv[1])
    else:
        f = open("test.txt")
    T = int(f.readline())
    data = list()
#    T = 2
    for i in range(T):
        A,B = map(int, f.readline().split())
        data.append((A, B))
        
    pool = Pool()
    result = pool.map(main, data)
#    result = map(main, data)
    for i in range(T):
        print "Case #%d: %s" % (i+1, result[i])