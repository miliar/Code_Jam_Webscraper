import sys

squares = []


def solve(r, p):
    i = 0
    x = (r + 1) ** 2 - r ** 2
    s = x
    while s <= p:
        x += 4
        s += x
        i += 1
    return i


def main(filename):
    with open(filename, "r") as f:
        T = int(f.readline().strip())
        for t in xrange(T):
            r, p = f.readline().strip().split(" ")
            sol = solve(long(r), long(p))
            print "Case #%d: %s" % (t+1, sol)


if __name__ == "__main__":
    main(sys.argv[1])
