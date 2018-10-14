

def min_opt(a, motes):
    if len(motes) == 0:
        return 0
    if a > motes[0]:
        return min_opt(a + motes[0], motes[1:])
    else:
        return 1 + min(min_opt(a + a - 1, motes), min_opt(a, motes[:-1]))


if __name__ == "__main__":
    f = open('1.in', 'r')
    o = open('1.out', 'w')

    T = int(f.readline().strip())

    for tcase in xrange(T):
        (a, n) = map(int, f.readline().strip().split(' '))
        motes = map(int, f.readline().strip().split(' '))
        motes.sort()
        # count = 0
        # idx = 0
        # while idx < n and count < n:
        #     if a > motes[idx]:
        #         a = a + motes[idx]
        #         idx = idx + 1
        #     else:
        #         a = a * 2 - 1
        #         count = count + 1
        if a == 1:
            count = n
        else:
            count = min_opt(a, motes)
        s = "Case #%s: %s\n" % (tcase + 1, count)
        o.write(s)
