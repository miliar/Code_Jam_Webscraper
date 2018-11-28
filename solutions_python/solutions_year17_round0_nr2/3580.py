import sys


if __name__ == '__main__':
    t = int(raw_input())
    for i in xrange(1, t + 1):
        n = int(raw_input())
        for j in xrange(n):
            j_str = "%d" % (n - j)
            valid = True
            for k in xrange(1, len(j_str)):
                if j_str[k-1] > j_str[k]:
                    valid = False
                    break
            if valid:
                break
        print "Case #%d: %d" % (i, n - j)

