import sys

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    T = int(f.readline())
    for _T in xrange(T):
        N = long(f.readline())

        if N < 10:
            ans = str(N)
        else:
            for n in xrange(N,0,-1):
                i_list = [long(x) for x in str(n)]
                if sorted(i_list) == i_list:
                    ans = n
                    break

        print "Case #%d: %s" % (_T + 1, ans)
