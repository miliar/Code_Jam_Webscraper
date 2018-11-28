from sys import stdin


def main():
    lines = stdin
    t = int(lines.next())
    for i in xrange(1, t + 1):
        smax_str, digits = lines.next().rstrip().split()
        smax = int(smax_str)
        s = [int(c) for c in digits]
        friends = 0
        total = 0
        for shyness, count in enumerate(s):
            if total + friends < shyness:
                friends += shyness - (total + friends)
            total += count
        print "Case #%d: %s" % (i, friends)
 

main()

