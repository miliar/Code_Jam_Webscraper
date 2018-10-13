from heapq import heappush, heappop

for case in range(1, int(input()) + 1):
    n, k = (int(x) for x in input().split())

    if n == k:
        print("Case #{}: 0 0".format(case))
    else:
        # Max-heap, lol
        gaps = [-n]

        for _k in range(k):
            split = -heappop(gaps) - 1
            last = (-(split // -2), split // 2)
            if last == (0, 0):
                break

            heappush(gaps, -last[0])
            heappush(gaps, -last[1])

        print("Case #{}: {} {}".format(case, last[0], last[1]))
