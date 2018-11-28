import sys

def process(c, f, x):

    prod = 2
    ct = 0

    total = x / prod

    while True:

        ct += c / prod

        prod += f

        total1 = x / prod + ct

        if total1 > total:
            break;

        total = total1

    return total


if __name__ == "__main__":

    f = sys.stdin

    if len(sys.argv) >= 2:

        fn = sys.argv[1]

        if fn != '-':
            f = open(fn)

    total = int(f.readline())

    for i in xrange(total):

        (c1, f1, x1) = ([float(j) for j in f.readline().split()])

        sec = process(c1, f1, x1)

        print "Case #%d: %.7f" % (i + 1, sec)
