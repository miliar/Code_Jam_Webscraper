import sys
import bisect

def line():
    return sys.stdin.readline().strip()

def ints(s):
    return [int(t) for t in s.split()]

def floats(s):
    return [float(t) for t in s.split()]


def find_gt(a,x):
    i = bisect.bisect_right(a, x)
    if i != len(a):
        return i
    return -1

def war(naomi0, ken0):
    naomi = sorted(naomi0)
    ken = sorted(ken0)

    r = 0
    while naomi:
        n = naomi[0]
        ki = find_gt(ken, n)
        if ki >= 0:
            naomi.remove(n)
            ken.remove(ken[ki])
        else:
            r += 1
            naomi.remove(n)
            ken.remove(ken[0])

    return r

def dwar(naomi0,ken0):
    eps = 0.000001
    naomi = sorted(naomi0)
    ken = sorted(ken0)

    km = max(ken)
    ni = find_gt(naomi,km)

    r = 0
    while naomi:
        km = ken[-1]
        nm = naomi[-1]

        if nm > km:
            r += 1
            naomi.remove(nm)
            ken.remove(km)
        else:
            naomi.remove(naomi[0])
            ken.remove(km)
    return r

def main():
    tc = int(line())
    for i in range(1,tc+1):
        line()
        naomi = floats(line())
        ken   = floats(line())
        print 'Case #%s: %s %s' % (i, dwar(naomi,ken), war(naomi,ken))


main()
