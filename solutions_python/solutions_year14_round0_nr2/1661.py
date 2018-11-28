import sys


def foo(ifile):
    a = [float(x) for x in ifile.readline().split()]
    res = a[2] / 2.0
    curSpeed = 2.0
    curTime = 0.0
    while True:
        curTime += a[0] / curSpeed
        curSpeed += a[1]
        tRes = curTime + a[2]/curSpeed
        if tRes < res:
            res = tRes
        else:
            return "%.7f" % res


def main(ifile):
    n = int(ifile.readline().strip())
    for i in range(n):
        print 'Case #%s: %s' % (i+1, foo(ifile))

main(sys.stdin)

