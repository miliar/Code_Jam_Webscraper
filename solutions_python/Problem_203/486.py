class Solution(object):
    def __init__(self):
        self._test_cases = self._read_int()

    def solve(self):
        for case_index in range(1, self._test_cases + 1):
            test_input = self._read_input_for_single_test_case()
            result = self._solve_single_test_case(test_input)
            self._process_single_test_case_output(case_index, result)

    def _read_input_for_single_test_case(self):
        r, c = self._read_int_array()
        test_input = [self._read_string() for _ in xrange(0, r)]
        pos = []
        for i in xrange(0, len(test_input)):
            for j in xrange(0, len(test_input[i])):
                if test_input[i][j] != '?':
                    pos.append([test_input[i][j], i, j])
        return test_input, pos

    def _solve_single_test_case(self, test_input):
        matrix, pos = test_input
        result = None

        pos = sorted(pos, key=lambda x: (x[1], x[2]))
        for p in pos:

            first_j, last_j = p[2] - 1, p[2] + 1
            while first_j > 0 and matrix[p[1]][first_j] == '?':
                first_j -= 1
            if first_j < 0 or matrix[p[1]][first_j] != '?':
                first_j += 1

            while last_j < len(matrix[0]) and matrix[p[1]][last_j] == '?':
                last_j += 1

            first_i, last_i = p[1] - 1, p[1] + 1
            while first_i > 0 and set(matrix[first_i][first_j:last_j]) in [set(['?']), set(['?', p[0]])]:
                first_i -= 1
            if first_i < 0 or set(matrix[first_i][first_j:last_j]) not in [set(['?']), set(['?', p[0]])]:
                first_i += 1

            while last_i < len(matrix) and set(matrix[last_i][first_j:last_j]) in [set(['?']), set(['?', p[0]])]:
                last_i += 1

            for i in xrange(first_i, last_i):
                for j in xrange(first_j, last_j):
                    matrix[i] = matrix[i][:first_j] + ''.join(p[0] for _ in xrange(last_j - first_j)) + matrix[i][
                                                                                                        last_j:]

        return '\n' + '\n'.join(matrix)

    @staticmethod
    def _test(pos, k):
        return len(set(map(lambda x: x[2], pos[:k + 1]))) == 1

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
