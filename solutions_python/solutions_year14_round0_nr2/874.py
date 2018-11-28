import heapq


def solve(c, f, x):
    q = [(0., 0., 2)]
    while q:
        time, balance, cookies_per_second = heapq.heappop(q)
        if balance >= x:
            return time

        wait_farm = c / cookies_per_second
        wait_x = (x - balance) / cookies_per_second
        heapq.heappush(q, (time + wait_farm, balance, cookies_per_second + f))
        heapq.heappush(q, (time + wait_x, x, cookies_per_second + f))


if __name__ == "__main__":
    t = int(raw_input())
    for i in xrange(t):
        c, f, x = map(float, raw_input().split())
        print("Case #{0}: {1:.7f}".format(i + 1, solve(c, f, x)))
