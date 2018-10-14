import sys

if __name__ == '__main__':
    f = open(sys.argv[1])
    T = int(f.readline())

    for i in xrange(1, T+1):
        n, k = f.readline().split()
        if int(k) % 2 ** int(n) == 2 ** int(n) - 1:
            print "Case #%s: ON" % i
        else:
            print "Case #%s: OFF" % i
    
