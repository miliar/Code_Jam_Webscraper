from heapq import heappush, heappop


def solve(n, k):
    if n == k or n == k - 1:
        return (0,0)

    heap = []
    heappush(heap, -1 * n)
    mx, mn = 0, 0
    while k > 0:
        biggest = -1 * heappop(heap)
        mx = biggest // 2
        if biggest % 2 == 1:
            mn = mx
        else:
            mn = max(mx - 1, 0)
        k -= 1
        heappush(heap, -1 * mx)
        heappush(heap, -1 * mn)
    return (mx, mn)

N = int(input().strip())
for i in range(0, N):
    case = input().strip().split(" ")
    mx, mn = solve(int(case[0]), int(case[1]))
    print("Case #{}: {} {}".format(i + 1, mx, mn))
