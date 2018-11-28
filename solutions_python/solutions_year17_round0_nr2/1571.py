from solution import Solution
from util import get_digits

# 1324141
# 1299999

# 1344141
# 1339999

# 1234561


class TidyNumbers(Solution):

    @staticmethod
    def _find_tidy_number(n):
        tidy_digits = []
        digits = get_digits(n)
        cur_len = 0
        for digit, digit2 in zip(digits[:-1], digits[1:]):
            cur_len += 1
            if digit < digit2:
                tidy_digits.extend(cur_len*[digit])
                cur_len = 0
            if digit > digit2:
                tidy_digits.append(digit-1)
                tidy_digits.extend((len(digits)-len(tidy_digits))*[9])
                break
        tidy_digits.extend((len(digits)-len(tidy_digits))*[digits[-1]])
        return int("".join(str(c) for c in tidy_digits))

    def parse_line(self, line):
        return int(line.strip())

    def run(self):
        self.results = [self._find_tidy_number(n) for n in self.inputs]


TidyNumbers("B-large")
