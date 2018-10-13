import sys

def is_on(n, k):
    upper_n = k ^ (k >> n << n)
    upper_n_full = upper_n == (1 << n) - 1

    return upper_n and upper_n_full

if __name__ == "__main__":
    file = sys.argv[1]

    with open(file) as fp:
        nrow = int(next(fp))

        for i in xrange(nrow):
            n, k = map(int, next(fp).strip().split())
            print "Case #%d: %s" % (i+1, "ON" if is_on(n, k) else "OFF")
