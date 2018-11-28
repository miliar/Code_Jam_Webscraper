from sys import stdin

def deceitful(naomi, ken):
    offset = 0

    while offset < len(naomi):
        if naomi[-offset - 1] < ken[-offset - 1]:
            naomi = naomi[1:]
            ken = ken[:-1]
        else:
            offset += 1

    return offset

def war(naomi, ken):
    points = 0

    for n in naomi:
        point = 1

        for k, i in zip(ken, xrange(len(ken))):
            if k > n:
                point = 0
                del ken[i]
                break

        points += point


    return points


T = int(stdin.readline())

for k in xrange(T):
    N = int(stdin.readline())
    naomi = map(float, stdin.readline().split())
    ken = map(float, stdin.readline().split())

    naomi.sort()
    ken.sort()

    print 'Case #%d:' % (k+1), deceitful(naomi, ken), war(naomi, ken)
