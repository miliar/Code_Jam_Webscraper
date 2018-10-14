import heapq
import unittest


def main():
    t_case = int(input())
    for i in range(t_case):
        n, k = map(int, input().split())
        l, s = solve(n, k)
        print("Case #{}: {} {}".format(i + 1, l, s))


def solve(n, k):
    l, s = 0, 0
    heap = [-n]
    heapq.heapify(heap)
    for i in range(k):
        temp = abs(heapq.heappop(heap))
        l, s = split(temp)
        heapq.heappush(heap, -l)
        heapq.heappush(heap, -s)
    return l, s


def split(n):
    k = (n - 1) // 2
    l, s = n - 1 - k, k
    return max(l, s), min(l, s)


if __name__ == "__main__":
    import sys

    sys.stdin = open("C-small-2-attempt0.in", 'r')
    sys.stdout = open("temp.out", 'w')
    main()


class TestMethods(unittest.TestCase):
    def test_split(self):
        self.assertEqual(split(2), (1, 0))
        self.assertEqual(split(3), (1, 1))
        self.assertEqual(split(1000), (500, 499))

    def test_solve(self):
        self.assertEqual(solve(4, 2), (1, 0))
        self.assertEqual(solve(5, 2), (1, 0))
        self.assertEqual(solve(6, 2), (1, 1))
        self.assertEqual(solve(1000, 1000), (0, 0))
        self.assertEqual(solve(1000, 1), (500, 499))
