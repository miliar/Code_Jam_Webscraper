cases = input()
for case in xrange(1, cases + 1):
    N, P = map(int, raw_input().split())
    G = [g % P for g in map(int, raw_input().split())]

    counts = [0] * P
    for g in G:
        counts[g] += 1

    solution = counts[0]

    if P == 2:
        solution += (counts[1]+1) / 2
    elif P == 3:
        if counts[1] <= counts[2]:
            counts[2] -= counts[1]
            solution += counts[1]
            solution += (counts[2]+2) / 3
        else:
            counts[1] -= counts[2]
            solution += counts[2]
            solution += (counts[1]+2) / 3

    print 'Case #%d: %d' % (case, solution)

