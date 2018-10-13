import heapq


def isclose(a, b, epsilon=1e-06):
    return abs(a - b) <= epsilon


T = int(raw_input())
for t in xrange(1, T + 1):
    N, K = map(int, raw_input().split(' '))
    assert N == K

    U = float(raw_input())
    P = map(float, raw_input().split(' '))
    assert len(P) == N
    heapq.heapify(P)

    while not isclose(U, 0):
        min_value = heapq.heappop(P)
        count = 1
        while len(P) > 0 and isclose(P[0], min_value):
            heapq.heappop(P)
            count += 1

        delta = min(1 - min_value if len(P) == 0 else P[0] - min_value,
                    U / count)
        new_value = min_value + delta
        for _ in xrange(count):
            heapq.heappush(P, new_value)
        U -= count * delta

    print 'Case #{}: {}'.format(t, reduce(lambda x, y: x * y, P))
