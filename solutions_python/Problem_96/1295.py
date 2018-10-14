import sys

def foo(ifile):
    aa = [int(x) for x in ifile.readline().split()]
    N, s, p = aa[:3]
    aa = aa[3:]

    if p == 0:
        a_max = 0
        a_min = 0
    elif p == 1:
        a_max = 1
        a_min = 1
    else:
        a_max = p * 3 - 2
        a_min = p * 3 - 4

    return len([x for x in aa if x >= a_max]) + min(s, len([x for x in aa if a_min <= x < a_max]))


def main(ifile, ofile):
    n = int(ifile.readline())
    for i in range(n):
        print 'Case #%s: %s' % (i+1, foo(ifile))

main(sys.stdin, sys.stdout)

