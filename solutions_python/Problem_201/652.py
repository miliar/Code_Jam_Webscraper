import random
import typing
import unittest


class Solution:

    def get_values_from_range_size(self, n) -> typing.Tuple[int, int]:
        n -= 1
        return (n // 2) + n % 2, n // 2

    def solve(self, n, k) -> typing.Tuple[int, int]:
        occupied = 0
        next_wave = 1

        while occupied + next_wave < k:
            occupied += next_wave
            next_wave *= 2

        remaining_people = k - occupied
        smaller_range = (n - occupied) // (occupied + 1)
        num_larger_range = (n - occupied) - (smaller_range * (occupied + 1))

        if remaining_people <= num_larger_range:
            return self.get_values_from_range_size(smaller_range + 1)
        return self.get_values_from_range_size(smaller_range)

    def get_ls(self, occupied) -> typing.List[int]:
        ls = [0] * len(occupied)
        for i in range(1, len(occupied)):
            if occupied[i - 1]:
                ls[i] = 0
            else:
                ls[i] = ls[i - 1] + 1
        return ls

    def get_rs(self, occupied) -> typing.List[int]:
        rs = [0] * len(occupied)
        for i in reversed(range(len(occupied) - 1)):
            if occupied[i + 1]:
                rs[i] = 0
            else:
                rs[i] = rs[i + 1] + 1
        return rs

    def find_best_stall(self, occupied, values) -> int:
        index = -1

        for i, v in enumerate(values):
            if occupied[i]:
                continue

            if index == -1:
                index = i
            elif min(v) > min(values[index]):
                index = i
            elif min(v) == min(values[index]) and max(v) > max(values[index]):
                index = i

        return index

    def solve_brute(self, n, k) -> typing.Tuple[int, int]:
        occupied = [False] * n

        for i in range(k):
            values = list(zip(self.get_ls(occupied), self.get_rs(occupied)))
            next_stall = self.find_best_stall(occupied, values)
            occupied[next_stall] = True

        ls, rs = values[next_stall]
        return max(ls, rs), min(ls, rs)


class TestSolution(unittest.TestCase):

    def test_example_1(self):
        n = 4
        k = 2
        expected = (1, 0)
        actual = Solution().solve(n, k)
        self.assertEqual(expected, actual)
        self.assertEqual(actual, Solution().solve_brute(n, k))

    def test_example_2(self):
        n = 5
        k = 2
        expected = (1, 0)
        actual = Solution().solve(n, k)
        self.assertEqual(expected, actual)
        self.assertEqual(actual, Solution().solve_brute(n, k))

    def test_example_3(self):
        n = 6
        k = 2
        expected = (1, 1)
        actual = Solution().solve(n, k)
        self.assertEqual(expected, actual)
        self.assertEqual(actual, Solution().solve_brute(n, k))

    def test_example_4(self):
        n = 1000
        k = 1000
        expected = (0, 0)
        actual = Solution().solve(n, k)
        self.assertEqual(expected, actual)
        self.assertEqual(actual, Solution().solve_brute(n, k))

    def test_example_5(self):
        n = 1000
        k = 1
        expected = (500, 499)
        actual = Solution().solve(n, k)
        self.assertEqual(expected, actual)
        self.assertEqual(actual, Solution().solve_brute(n, k))

    def test_example_6(self):
        n = 10 ** 18
        k = 10 ** 18
        expected = (0, 0)
        actual = Solution().solve(n, k)
        self.assertEqual(expected, actual)

    def test_exhaustive(self):
        ns = [100, 101, 128, 127, 129]

        for n in ns:
            for k in range(1, n + 1):
                expected = Solution().solve_brute(n, k)
                actual = Solution().solve(n, k)
                self.assertEqual(expected, actual)


if __name__ == "__main__":
    t = int(input())
    for test_case in range(t):
        n, k = (int(num) for num in input().split())
        solution = Solution().solve(n, k)

        print("Case #{}: {} {}".format(test_case + 1, solution[0], solution[1]))
