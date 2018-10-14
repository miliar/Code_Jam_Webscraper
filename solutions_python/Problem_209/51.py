import math
import queue


def get_side_area(r, h):
    return 2 * r * h


def get_top_area(r):
    return r * r


def answer(k, rhs):
    n = len(rhs)

    rhs.sort()

    max_area = 0
    total_side_area = 0
    q = queue.PriorityQueue()

    for i, (r, h) in zip(range(1, n + 1), rhs):
        if i > k:
            total_side_area -= q.get_nowait()
        side_area = get_side_area(r, h)
        total_side_area += side_area
        q.put_nowait(side_area)

        if i >= k:
            current_area = total_side_area + get_top_area(r)
            max_area = max(max_area, current_area)

    return max_area * math.pi


def read_ints():
    return tuple(int(j) for j in input().split(" "))


def main():
    t = int(input())
    for i in range(1, t + 1):
        n, k = read_ints()
        rhs = []
        for j in range(n):
            r, h = read_ints()
            rhs.append((r, h))

        result = answer(k, rhs)
        print("Case #{}: {:.8f}".format(i, result))


if __name__ == "__main__":
    main()
