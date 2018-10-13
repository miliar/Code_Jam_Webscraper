import sys

def simulateSnaps(snappers, snaps):
    t = 2 ** snappers
    x = snaps & t - 1
    return x + 1 == t

def main(fn):
    with open(fn) as f:
        lines = int(f.readline())
        for x in xrange(lines):
            z = map(int, f.readline().split())
            r = simulateSnaps(z[0], z[1])
            r = "ON" if r else "OFF"
            print "Case #%s: %s" % (x + 1, r)

if __name__ == "__main__":
    if len(sys.argv) ==  2:
        main(sys.argv[1])
    else:
        print "Usage: %s --in=<input_file>" % sys.argv[0]

