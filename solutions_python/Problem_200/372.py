class Solution(object):
    def __init__(self):
        self._test_cases = self._read_int()

    def solve(self):
        for case_index in range(1, self._test_cases + 1):
            test_input = self._read_input_for_single_test_case()
            result = self._solve_single_test_case(test_input)
            self._process_single_test_case_output(case_index, result)

    def _read_input_for_single_test_case(self):
        return map(lambda c: int(c), self._read_string())

    @staticmethod
    def _solve_single_test_case(test_input):
        if len(test_input) == 1:
            return test_input[0]
        idx = 0
        while idx + 1 < len(test_input) and test_input[idx] <= test_input[idx + 1]:
            idx += 1

        if idx == len(test_input) - 1:
            return reduce(lambda a, b: 10 * a + b, test_input)
        result = 0
        if idx == 0:
            k = len(test_input) - 1
            if test_input[idx] > 1:
                result = (10 ** k) * (test_input[idx] - 1)
            result += (10 ** k) - 1
        elif test_input[idx] > test_input[idx - 1]:
            result = reduce(lambda a, b: 10 * a + b,
                            test_input[:idx] + [test_input[idx] - 1] + map(lambda x: 9, test_input[idx + 1:]))
        else:
            while idx > 0 and test_input[idx] == test_input[idx - 1]:
                idx -= 1
            if idx > 0:
                result = reduce(lambda a, b: 10 * a + b,
                                test_input[:idx] + [test_input[idx] - 1] + map(lambda x: 9, test_input[idx + 1:]))
            else:
                result = reduce(lambda a, b: 10 * a + b, [test_input[0] - 1] + map(lambda x: 9, test_input[1:]))

        return result

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
