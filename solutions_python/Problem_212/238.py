class Solution(object):
    def __init__(self):
        self._test_cases = self._read_int()

    def solve(self):
        for case_index in range(1, self._test_cases + 1):
            test_input = self._read_input_for_single_test_case()
            result = self._solve_single_test_case(test_input)
            self._process_single_test_case_output(case_index, result)

    def _read_input_for_single_test_case(self):
        N, P = self._read_int_array()
        groups = self._read_int_array()

        # Implement input read here

        return P, groups

    def _solve_single_test_case(self, test_input):
        P, groups = test_input
        result = len(filter(lambda x: x % P == 0, groups))
        groups = filter(lambda x: x % P > 0, groups)
        if P == 2:
            result += (len(groups) + 1) / 2
        elif P == 3:
            r1 = len(filter(lambda x: x % P == 1, groups))
            r2 = len(filter(lambda x: x % P == 2, groups))
            result += min(r1, r2)
            a = abs(r1 - r2)
            result += (a + (P - a % P) % P) / P
        else:
            pass
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
