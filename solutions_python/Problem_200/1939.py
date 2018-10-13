import sys


class TestCase(object):
    def __init__(self, N):
        self._N = N

    def _get_number(self, digits):
        return int("".join([str(d) for d in digits]))

    def _get_digits(self, num):
        return [int(n) for n in list(str(num))]

    def _is_tidy(self, digits):
        for i in xrange(len(digits)-1):
            if digits[i] > digits[i+1]:
                return False, i
        return True, 0

    def _solve_aux(self, num):
        digits = self._get_digits(num)

        if len(digits) == 1:
            return num

        is_tidy, max_not_tidy = self._is_tidy(digits)
        if is_tidy:
            return num

        digits[max_not_tidy] -= 1
        for i in xrange(max_not_tidy+1, len(digits)):
            digits[i] = 9

        return self._solve_aux(self._get_number(digits))

    def solve(self):
        return self._solve_aux(self._N)

    def __str__(self):
        return "N: {}".format(self._N)


def parse(input_file_path):
    test_cases = []

    with open(input_file_path, "r") as input_file:
        test_cases_number = int(input_file.readline())
        for i in xrange(test_cases_number):
            line = input_file.readline()
            test_case = TestCase(N=int(line))
            test_cases.append(test_case)

    return test_cases


def main(input_file_path):
    test_cases = parse(input_file_path)

    for i, test_case in enumerate(test_cases):
        solution = test_case.solve()
        print "Case #{0}: {1}".format(i+1, solution)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))