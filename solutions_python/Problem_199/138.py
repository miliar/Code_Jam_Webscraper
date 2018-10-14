import StringIO

import itertools

from ecodejam.input_parser import *


def flip_k(pancakes, j, k):
    for i in xrange(j, j + k):
        pancakes[i] = "+" if pancakes[i] == "-" else "-"


def solve(case_index):
    print case_index
    pancakes = list(read_word())
    k = read_int()
    next_line()

    flips = 0
    for i in xrange(len(pancakes) - k + 1):
        if pancakes[i] == '-':
            flips += 1
            flip_k(pancakes, i, k)

    if "-" in pancakes[-k:]:
        return "IMPOSSIBLE"
    return str(flips)

    # return "{:.10}".format(max(tie_prob_for_option(k, option) for option in itertools.combinations(probs, k)))


SAMPLE = """
3
---+-++- 3
+++++ 4
-+-+- 4
"""

if __name__ == "__main__":
    set_parsed_input(
        StringIO.StringIO(SAMPLE)
    )
    run_solver(solve)
