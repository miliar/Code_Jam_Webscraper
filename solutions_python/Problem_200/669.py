import random
import unittest


class Solution:

    def solve(self, n) -> int:
        n_list = [int(d) for d in str(n)]
        for i in reversed(range(1, len(n_list))):
            if n_list[i] >= n_list[i - 1]:
                continue

            n_list[i - 1] -= 1
            for j in range(i, len(n_list)):
                n_list[j] = 9

        return int("".join(str(d) for d in n_list))


class TestSolution(unittest.TestCase):

    def test_example_1(self):
        n = 132
        expected = 129
        actual = Solution().solve(n)
        self.assertEqual(expected, actual)

    def test_example_2(self):
        n = 1000
        expected = 999
        actual = Solution().solve(n)
        self.assertEqual(expected, actual)

    def test_example_3(self):
        n = 7
        expected = 7
        actual = Solution().solve(n)
        self.assertEqual(expected, actual)

    def test_example_4(self):
        n = 111111111111111110
        expected = 99999999999999999
        actual = Solution().solve(n)
        self.assertEqual(expected, actual)

    def test_random_example(self):
        n = random.randint(1, 10 ** 18)
        actual = Solution().solve(n)
        print("solve({}) = {}".format(n, actual))


if __name__ == "__main__":
    t = int(input())
    for test_case in range(t):
        n = int(input())
        solution = Solution().solve(n)

        print("Case #{}: {}".format(test_case + 1, solution))
