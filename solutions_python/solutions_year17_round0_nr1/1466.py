def how_many(p, k):
    if (sum(p) == len(p)):
        return 0

    num = 0

    for i in xrange(len(p) - k + 1):
        if p[i] == 0 and sum(p[i:i + k]) != k:
            for j in xrange(k):
                p[i + j] = 1 - p[i + j]
            num += 1

    if sum(p) != len(p):
        return -1

    return num


t = int(raw_input())

for i in xrange(t):
    p, k = raw_input().split()

    k = int(k)
    
    b = [1 if x == '+' else 0 for x in p]

    num_flips = how_many(b, k)

    if (num_flips == -1):
        print 'Case #%d: IMPOSSIBLE' % (i + 1)
    else:
        print 'Case #%d: %d' % (i + 1, num_flips)