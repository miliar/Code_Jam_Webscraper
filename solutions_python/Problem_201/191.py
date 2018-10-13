# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
import heapq


def solve_slow(n, k):
    q = []
    heapq.heappush(q, -n)
    for __ in range(k):
        n = -heapq.heappop(q)
        heapq.heappush(q, -(n // 2))
        heapq.heappush(q, -((n - 1) // 2))
    return n // 2, (n - 1) // 2


def solve(n, k):
    if k > 4:
        if k % 2 == 1:
            return solve((n - 1) // 2, (k - 1) // 2)
        return solve(n // 2, (k - 1) // 2 + 1)
    return solve_slow(n, k)


def main():
    t = int(input())  # read a line with a single integer

    for i in range(1, t + 1):
        n, k = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
        a, b = solve(n, k)
        print("Case #{}: {} {}".format(i, a, b))


if __name__ == "__main__":
    main()
