
import sys, os.path

def solve(P, K, L, F):
    F.sort(reverse = True)
    n = 1
    c = 0
    for i, f in enumerate(F):
        if i >= n * K:
            n += 1
        c += n * f
    return c

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage: %s <input>" % sys.argv[0]
        sys.exit()
    fd = open(sys.argv[1], 'r')
    out = os.path.splitext(sys.argv[1])[0] + '.out'
    fd2 = open(out, 'w')
    n = int(fd.readline())
    for i in xrange(n):
        X = fd.readline().strip().split(' ')
        P, K, L = map(int, X)
        X = fd.readline().strip().split(' ')[:L]
        F = map(int, X)
        x = solve(P, K, L, F)
        fd2.write("Case #%i: %s\n" % (i + 1, x))
    fd.close()
    fd2.close()
