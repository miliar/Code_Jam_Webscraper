import sys

def test(n, k):
    if k == 0 or k < n:
#        print 'sai'
        return 'OFF'

    r = bin(k%(2**n)).split('b')[1]
#    print r
    if len(r) < n:
        return 'OFF'

    for i in xrange(len(r)):
        if r[i] != '1':
            return 'OFF'
    return 'ON'


if __name__ == "__main__":
    fileIn = sys.stdin
    T = int(fileIn.readline())

    for i in xrange(1,T+1):

        N, K = fileIn.readline().split()
        N, K = int(N), int(K)
        print "Case #%d:" % i,
        print test(N,K)




