import sys


def solve(mini, maxi):
    #print mini, maxi
    counter = 0
    #store = set()
    swap_len = len(str(mini))
    for n in xrange(mini, maxi):
        sn = str(n)
        for m in xrange(n + 1, maxi + 1):
            sm = str(m)
            for i in xrange(swap_len):
                r = sn[i:] + sn[:i]
                if r == sm:
                    counter += 1
                    #store.add(r)
                    #print "   ", i, ": ", r, sm, "?", r == sm
                    break
    return counter


def main(filename):
    with open(filename, "r") as f:
        T = int(f.readline().strip())
        for t in xrange(1, T + 1):
            mini, maxi = [int(x) for x in f.readline().strip().split(" ")]
            print "Case #%d: %s" % (t, solve(mini, maxi))

if __name__ == "__main__":
    main(sys.argv[1])
