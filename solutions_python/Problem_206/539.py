import sys

DEBUG=True
DEBUG=False

def solve(d, h):
    max_t = max([(d-k)*1.0/s for k,s in h])
    return "%.6f" % (d/max_t)

if __name__ == "__main__":
    i = 1
    data = sys.stdin.read().split()
    for _ in xrange(int(data.pop(0))):
        d = int(data.pop(0))
        n = int(data.pop(0))
        h = []
        for _ in range(n):
            h.append([int(data.pop(0)), int(data.pop(0))])
        print "Case #%d: %s" % (i, solve(d, h))
        i += 1
