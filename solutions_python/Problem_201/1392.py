import heapq

n = int(input())
cases = []
for _ in range(n):
    N, K = input().split()
    N, K = int(N), int(K)
    cases.append((N, K))


def do(n, k):
    gaps = [-n]
    for _ in range(k):
        old = -heapq.heappop(gaps)
        big, small = int((old+0.5)//2), int((old-0.5)//2)
        if big > 0:
            heapq.heappush(gaps, -big)
        if small > 0:
            heapq.heappush(gaps, -small)
    return big, small


if __name__ == "__main__":
    for index, (n, k) in enumerate(cases):
        y, z = do(n, k)
        print("Case #{}: {} {}".format(index+1, y, z))
