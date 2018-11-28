
import math


def do_p(pancakes, K, previous, first):
    if K == 0:
        return previous[0] ** 2 * math.pi
    if not pancakes:
        return 0

    pancakes = list(pancakes)

    n = pancakes[0]
    pancakes.pop(0)
    area = n[1] * (n[0] * 2 * math.pi)
    diff = previous[0] - n[0]
    if diff > 0 and not first:
        area += previous[0] ** 2 * math.pi - n[0] ** 2 * math.pi

    # if previous[0] == n[0]:
    return max(do_p(pancakes, K-1, n, False) + area, do_p(pancakes, K, previous, first))
    # else:
    #     return do_p(pancakes, K-1, n)


T = int(input())
for i in range(0, T):
    data = list(map(int, input().split()))
    N = data[0]
    K = data[1]

    pancakes = []
    for j in range(N):
        size = list(map(int, input().split()))
        pancakes.append((size[0], size[1]))

    pancakes.sort(key=lambda x: x[1], reverse=True)
    pancakes.sort(reverse=True)

    # pancakes1 = pancakes
    #
    # best = 0
    # for k in range(0, N - K + 1):
    #     pancakes = pancakes1[k:]
    #     area = 0
    #     previous = pancakes[0]
    #     for j in range(K):
    #         n = pancakes[0]
    #         pancakes.pop(0)
    #         area += n[1] * (n[0]*2*math.pi)
    #         diff = previous[0] - n[0]
    #         if diff > 0:
    #             area += previous[0]**2*math.pi - n[0]**2*math.pi
    #         previous = n
    #
    #     area += previous[0] ** 2 * math.pi
    #
        # if area > best:
        #     best = area

    best = 0
    for k in range(0, N - K + 1):
        area = do_p(pancakes[k:], K, (0, 0), True)
        if area > best:
            best = area

    print("Case #%d: %f" % ((i+1), best))