import heapq

def solve(n, k):
    heap = []
    heapq.heappush(heap, (-n, 0, n - 1))

    for i in range(k):
        data = heapq.heappop(heap)
        ls = data[1]
        rs = data[2]
        new_pos = (ls + rs) // 2
        heapq.heappush(heap, (-(new_pos - ls + 1), ls, new_pos))
        heapq.heappush(heap, (-(rs - new_pos + 1), new_pos, rs))

        ls = new_pos - ls - 1
        rs = rs - new_pos - 1

        f_min = min(ls, rs)
        f_max = max(ls, rs)

        if i == k - 1:
            return (f_max, f_min)
    return None

if __name__ == "__main__":
    tests = int(input())
    for test in range(tests):
        (n, k) = list(map(int, input().split()))
        answer = solve(n + 2, k)
        print("Case #" + str(test + 1) + ": " + str(answer[0]) + " " + str(answer[1]))

