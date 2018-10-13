class Solution(object):
    def __init__(self):
        self._test_cases = self._read_int()

    def solve(self):
        for case_index in range(1, self._test_cases + 1):
            test_input = self._read_input_for_single_test_case()
            result = self._solve_single_test_case(test_input)
            self._process_single_test_case_output(case_index, result)

    def _read_input_for_single_test_case(self):
        inp = self._read_string_array()
        tab = map(lambda c: 1 if c == '+' else 0, inp[0].strip('+'))
        return [tab, int(inp[1])]

    @staticmethod
    def _solve_single_test_case(test_input):
        tab = test_input[0]
        k = test_input[1]
        result = 0
        cur_pos = 0
        while cur_pos + k <= len(tab):
            next_pos = cur_pos + k
            if tab[cur_pos] % 2 == 0:
                result += 1
                unlocked = True
                for i in xrange(cur_pos, cur_pos + k):
                    tab[i] += 1
                    if tab[i] % 2 == 0 and unlocked:
                        next_pos = i
                        unlocked = False
                cur_pos = next_pos
            else:
                cur_pos += 1

        is_valid = len(filter(lambda x: x % 2 == 0, tab)) == 0
        return result if is_valid else "IMPOSSIBLE"

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
