def solve(N, naomi, ken):
    naomi = sorted(naomi)
    ken = sorted(ken)
    # print naomi
    # print ken
    j = z = 0
    for i, x in enumerate(naomi):
        while j < len(ken):
            if ken[j] > naomi[i]:
                z += 1
                j += 1
                break
            j += 1
    z = N - z

    y = 0
    for i, x in enumerate(naomi):
        if naomi[i] < ken[0]:
            del ken[-1]
            y += 1
        else:
            del ken[0]
    y = N - y
    return '%d %d' % (y, z)


def run():
    T = int(raw_input())
    for i in xrange(T):
        N = [float(x) for x in raw_input().split()][0]
        naomi = [float(x) for x in raw_input().split()]
        ken = [float(x) for x in raw_input().split()]
        r = solve(N, naomi, ken)
        print 'Case #%d:' % (i + 1),
        print r


if __name__ == '__main__':
    run()
