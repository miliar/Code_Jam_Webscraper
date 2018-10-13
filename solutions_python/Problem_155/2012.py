import sys

def process(maxshy, countshy):

    shyness = 0
    min = 0
    standing = 0

    for num in list(countshy):

        diff = shyness - standing

        if diff > 0:
            min = min + 1
            standing += 1

        standing += num
        shyness += 1

    return min


if __name__ == "__main__":

    f = sys.stdin

    if len(sys.argv) >= 2:

        fn = sys.argv[1]

        if fn != '-':
            f = open(fn)

    total = int(f.readline())

    for i in xrange(total):

        (maxshy, countshystr) = f.readline().split()

        countshy = [int(j) for j in list(countshystr)]

        minfriends = process(int(maxshy), countshy)

        print "Case #%d: %d" % (i + 1, minfriends)
