import heapq


def solve(actvs):
    actvs.sort()

    A = len(actvs)

    jtime = 720
    ctime = 720

    res = 0

    intervals = []
    for i in xrange(A):
        first = actvs[i]
        second = actvs[(i + 1) % A]

        if first[2] == 'C':
            jtime -= first[1] - first[0]
        else:
            ctime -= first[1] - first[0]

        if first[2] != second[2]:
            res += 1
        else:
            t = second[0] - first[1]
            if t < 0:
                t += 1440
            intervals.append((t, first[2]))

    h = intervals
    heapq.heapify(h)

    while len(h) > 0:
        elem = heapq.heappop(h)
        if elem[1] == 'C' and jtime < elem[0]:
            res += 2
            continue
        if elem[1] == 'J' and ctime < elem[0]:
            res += 2
            continue

        if elem[1] == 'J':
            ctime -= elem[0]
        else:
            jtime -= elem[0]

    return max(2, res)

T = int(raw_input())

for i in xrange(T):
    AC, AJ = [int(x) for x in raw_input().split()]

    actvs = []
    for j in xrange(AC):
        b, e = [int(x) for x in raw_input().split()]
        actvs.append([b, e, 'C'])
    for j in xrange(AJ):
        b, e = [int(x) for x in raw_input().split()]
        actvs.append([b, e, 'J'])

    print 'Case #%d: %d' % (i + 1, solve(actvs))
