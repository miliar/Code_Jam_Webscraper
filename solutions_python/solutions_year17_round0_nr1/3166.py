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

        print pancakes, out

    def case_samples(self):
        return [
            '---+-++- 3',
            '+++++ 4',
            '-+-+- 4',
        ]

    def case_files(self):
        return [
            '../data/2017-google-code-jam/round-q/A-small-attempt0.in',
            '../data/2017-google-code-jam/round-q/A-large-attempt0.in',
        ]


run(__name__)
