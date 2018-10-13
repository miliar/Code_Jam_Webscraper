import os, sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), '.'))
from core import *

# -----------------------------------------------------------------------------
# Round Q 2017
# Problem A. Oversized Pancake Flipper
# + (which represents a pancake that is initially happy side up)
# - (which represents a pancake that is initially blank side up).
# -----------------------------------------------------------------------------
def flip(pancakes, start, end):
    for index in xrange(start, end):
        if pancakes[index] == '+': pancakes[index] = '-'
        elif pancakes[index] == '-': pancakes[index] = '+'


def is_valid(pancakes):
    for state in pancakes:
        if pancakes[0] != state:
            return False
    return True


class PancakeFlipper(Solution):
    def handle(self, case):
        pancakes, flipper_size = case.case_input.split(' ')
        pancakes = [c for c in pancakes]
        flipper_size = int(flipper_size)

        flips = 0
        i = 0
        while (i + flipper_size) <= len(pancakes):
            if pancakes[i] != '+':
                flip(pancakes, i, i+flipper_size)
                flips += 1
            i += 1

        out = str(flips) if is_valid(pancakes) else 'IMPOSSIBLE'
        case.register_case_output(out)

    def case_samples(self):
        return [
            '---+-++- 3',
            '+++++ 4',
            '-+-+- 4',
        ]

    def case_files(self):
        return [
            '../data/2017-google-code-jam/round-q/A-small-attempt0.in',
            '../data/2017-google-code-jam/round-q/A-large.in',
        ]


# -----------------------------------------------------------------------------
# Round Q 2017
# Problem B. Tidy Numbers
# -----------------------------------------------------------------------------
class TidyNumbers(Solution):
    def handle(self, case):
        number = [int(digit) for digit in case.case_input]

        non_tidy_index = self.find_non_tidy_index(number)
        tidy_number = number if non_tidy_index == -1 else self.convert_to_tidy(number, non_tidy_index)

        out = str(int(''.join([str(digit) for digit in tidy_number])))
        case.register_case_output(out)

    def convert_to_tidy(self, candidate, non_tidy_index):
        number = candidate[:]
        number[non_tidy_index] -= 1
        for index in xrange(non_tidy_index + 1, len(number)):
            number[index] = 9
        return number

    def find_non_tidy_index(self, number):
        tidy_index = 0
        pivot = -1
        for index, digit in enumerate(number):
            if digit < pivot:
                return tidy_index
            if pivot != digit:
                tidy_index = index
            pivot = digit
        return -1

    def case_samples(self):
        return [
            '132',
            '1000',
            '7',
            '111111111111111110',
            '129',
            '109',
        ]

    def case_files(self):
        return [
            '../data/2017-google-code-jam/round-q/B-small-attempt0.in',
            '../data/2017-google-code-jam/round-q/B-large.in',
        ]


run(__name__)
