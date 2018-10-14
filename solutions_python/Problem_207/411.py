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

    def _solve_single_test_case(self, test_input):
        N, R, O, Y, G, B, V = test_input
        result = ''
        last = ''
        while len(result) < N:
            next = self._get_next(R, G, Y, V, B, O, last, result[0] if len(result) > 0 else '')
            if next == 'G':
                G -= 1
                R -= 1
                result += 'GR'
                last = 'R'
            elif next == 'V':
                V -= 1
                Y -= 1
                result += 'VY'
                last = 'Y'
            elif next == 'O':
                O -= 1
                B -= 1
                result += 'OB'
                last = 'B'
            else:
                if next == 'R':
                    if R > 0:
                        result += 'R'
                        R -= 1
                        last = 'R'
                    else:
                        return 'IMPOSSIBLE'
                elif next == 'Y':
                    if Y > 0:
                        result += 'Y'
                        Y -= 1
                        last = 'Y'
                    else:
                        return 'IMPOSSIBLE'
                elif B > 0:
                    result += 'B'
                    B -= 1
                    last = 'B'
                else:
                    return 'IMPOSSIBLE'
        if result[-1] == 'Y' and Y == -1 and result[-2] == 'V':
            result = result[:-1]
        elif result[-1] == 'B' and B == -1 and result[-2] == 'O':
            result = result[:-1]
        elif result[-1] == 'R' and R == -1 and result[-2] == 'G':
            result = result[:-1]
        return result if result[-1] != result[0] and len(result) == N else 'IMPOSSIBLE'

    def _get_next(self, R, G, Y, V, B, O, last, first):
        if last == 'R' and G > 0:
            return 'G'
        if last == 'Y' and V > 0:
            return 'V'
        if last == 'B' and O > 0:
            return 'O'
        t = sorted([['R', R + G], ['Y', Y + V], ['B', B + O]], key=lambda x: x[1], reverse=True)
        for i, k in enumerate(t):
            if first != '' and first != last and i+1 <len(t) and t[i+1][1] == k[1] and t[i+1][0] == first and sum([t[0][1], t[1][1], t[2][1]]) == 2:
                return first
            if k[0] != last:
                return k[0]

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
