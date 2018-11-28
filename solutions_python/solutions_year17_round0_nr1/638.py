import random
import unittest


class Solution:

    def flip(self, the_list, index) -> None:
        the_list[index] = '+' if the_list[index] == '-' else '-'

    def solve(self, s, k) -> int:
        num_flips = 0
        s_list = list(s)
        for i in range(len(s_list) - k + 1):
            if s_list[i] == '-':
                for j in range(i, i + k):
                    self.flip(s_list, j)
                num_flips += 1

        if "".join(s_list) == "+" * len(s):
            return num_flips
        return -1

    def solve_brute(self, s, k) -> int:
        target = "+" * len(s)
        current_set = {s}
        current_flips = 0
        visited = {s}

        while current_set and target not in current_set:
            next_set = set()
            for elem in (list(e) for e in current_set):
                for i in range(k):
                    self.flip(elem, i)

                new_elem = "".join(elem)
                if new_elem not in visited:
                    next_set.add(new_elem)
                    visited.add(new_elem)

                for i in range(1, len(elem) - k + 1):
                    self.flip(elem, i - 1)
                    self.flip(elem, i + k - 1)
                    new_elem = "".join(elem)
                    if new_elem not in visited:
                        next_set.add(new_elem)
                        visited.add(new_elem)

            current_flips += 1
            current_set = next_set

        if current_set:
            return current_flips
        return -1


class TestSolution(unittest.TestCase):

    def test_example_1(self):
        s = "---+-++-"
        k = 3
        expected = 3
        actual = Solution().solve(s, k)
        self.assertEqual(expected, actual)
        self.assertEqual(actual, Solution().solve_brute(s, k))

    def test_example_2(self):
        s = "+++++"
        k = 4
        expected = 0
        actual = Solution().solve(s, k)
        self.assertEqual(expected, actual)
        self.assertEqual(actual, Solution().solve_brute(s, k))

    def test_example_3(self):
        s = "-+-+-"
        k = 4
        expected = -1
        actual = Solution().solve(s, k)
        self.assertEqual(expected, actual)
        self.assertEqual(actual, Solution().solve_brute(s, k))

    def test_big_example(self):
        s = "".join(random.choice(['+', '-']) for _ in range(1000))
        k = 500
        expected = -1
        actual = Solution().solve(s, k)
        self.assertEqual(expected, actual)

    def test_big_example_with_solution(self):
        s = ['+'] * 1000
        k = 500
        for _ in range(1000):
            index = random.randint(0, len(s) - k)
            for i in range(index, index + k):
                Solution().flip(s, i)

        actual = Solution().solve("".join(s), k)
        print(actual)


if __name__ == "__main__":
    t = int(input())
    for test_case in range(t):
        s, k = input().split()
        k = int(k)
        solution = Solution().solve(s, k)

        print("Case #{}: ".format(test_case + 1), end='')
        if solution != -1:
            print(solution)
        else:
            print("IMPOSSIBLE")
