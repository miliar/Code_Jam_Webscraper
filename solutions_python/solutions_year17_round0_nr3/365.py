class Solution(object):
    def __init__(self):
        self._test_cases = self._read_int()

    def solve(self):
        for case_index in range(1, self._test_cases + 1):
            test_input = self._read_input_for_single_test_case()
            result = self._solve_single_test_case(test_input)
            self._process_single_test_case_output(case_index, result)

    def _read_input_for_single_test_case(self):
        return self._read_int_array()

    @staticmethod
    def _solve_single_test_case(test_input):
        n, x = test_input

        result = None
        k = 0
        while x >= 2 ** (k + 1):
            k += 1

        p = n / (2 ** k)
        a = (2 ** k) * (p + 1) - n - 1
        b = 2 ** k - a
        x -= 2 ** k

        partial = p if x < b else p - 1
        result = [partial / 2, (partial - 1) / 2]

        return '{} {}'.format(result[0], result[1])

    @staticmethod
    def _process_single_test_case_output(case_index, result):
        print('Case #{}: {}'.format(case_index, result))

    @staticmethod
    def _read_int():
        return int(raw_input().strip())

    @staticmethod
    def _read_int_array():
        return map(int, raw_input().strip().split())

    @staticmethod
    def _read_string():
        return raw_input().strip()

    @staticmethod
    def _read_string_array():
        return raw_input().strip().split()


solution = Solution()
solution.solve()
