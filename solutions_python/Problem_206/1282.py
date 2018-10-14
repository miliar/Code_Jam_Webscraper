import typing
import unittest


Horse = typing.NamedTuple("Horse", [('k', int), ('s', int)])


class Solution:

    def solve(self, d: int, n: int, horses) -> float:
        times = map(lambda horse: (d - horse.k) / horse.s, horses)
        speed = d / max(times)
        return speed


class TestSolution(unittest.TestCase):

    def test_example_1(self):
        d = 2525
        n = 1
        horses = [Horse(2400, 5)]
        expected = 101
        actual = Solution().solve(d, n, horses)
        self.assertAlmostEqual(expected, actual)

    def test_example_2(self):
        d = 300
        n = 2
        horses = [Horse(120, 60), Horse(60, 90)]
        expected = 100
        actual = Solution().solve(d, n, horses)
        self.assertAlmostEqual(expected, actual)

    def test_example_3(self):
        d = 100
        n = 2
        horses = [Horse(80, 100), Horse(70, 10)]
        expected = 33.333333333
        actual = Solution().solve(d, n, horses)
        self.assertAlmostEqual(expected, actual)


if __name__ == "__main__":
    t = int(input())
    for test_case in range(t):
        d, n = (int(num) for num in input().split())
        horses = []
        for _ in range(n):
            line = input()
            k, s = line.split(' ')
            horses.append(Horse(int(k), int(s)))
        solution = Solution().solve(d, n, horses)

        print("Case #{}: {}".format(test_case + 1, solution))
