PI = 3.141592653589793


class Solution(object):
    def __init__(self):
        self._test_cases = self._read_int()

    def solve(self):
        for case_index in range(1, self._test_cases + 1):
            test_input = self._read_input_for_single_test_case()
            result = self._solve_single_test_case(test_input)
            self._process_single_test_case_output(case_index, result)

    def _read_input_for_single_test_case(self):
        N, K = self._read_int_array()
        pancakes = [self._read_int_array() for _ in xrange(N)]

        return K, sorted(pancakes, key=lambda x: (x[0], x[1]), reverse=True)

    def _solve_single_test_case(self, test_input):
        K, pancakes = test_input
        result = 0

        for i in xrange(len(pancakes)):
            p_result = self._side(pancakes[i][0], pancakes[i][1]) + self._plane(pancakes[i][0])
            if K > 1:
                partial = sorted(pancakes[i + 1:], key=lambda x: self._side(x[0], x[1]), reverse=True)
                if len(partial) >= K - 1:
                    p_result += sum(map(lambda x: self._side(x[0], x[1]), partial[:K - 1]))
                    if p_result > result:
                        result = p_result
            elif p_result > result:
                result = p_result

        return result

    def _plane(self, R):
        return PI * R * R

    def _side(self, R, H):
        return 2.0 * PI * R * H

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
