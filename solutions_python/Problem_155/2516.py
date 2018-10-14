T = int(raw_input())
t = 1
while t <= T:
    S_max, Ss = raw_input().strip().split(' ')
    needed = 0
    standing = 0
    for idx, n in enumerate(Ss):
        n = int(n)
        added = 0
        if standing < idx and n > 0:
            added = (idx - standing)

        standing += n + added
        needed += added
        # print 'idx, n, standing, needed = ', idx, n, standing, needed

    print 'Case #{}: {}'.format(t, needed)
    t += 1


