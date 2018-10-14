import StringIO

import math

from ecodejam.input_parser import read_int, set_parsed_input, run_solver, next_line


def calc_area_for_stack(stack):
    stack = sorted(stack, key=lambda cake: cake["r"], reverse=True)

    return stack[0]["r"] * stack[0]["r"] + sum(2 * cake["r"] * cake["h"] for cake in stack)


def solve(case_index):
    n = read_int()
    k = read_int()
    next_line()

    cakes = [

    ]

    for i in xrange(n):
        cakes.append({
            "r": float(read_int()),
            "h": float(read_int()),
        })

    options = []

    for i in xrange(n):
        lead = cakes[i]
        # Test pancake i as first
        chosen = [lead] + sorted((cake for cake in cakes if cake["r"] <= lead["r"] and cake is not lead), key=lambda cake: cake["h"] * cake["r"], reverse=True)[:k - 1]

        if len(chosen) < k:
            continue

        options.append(calc_area_for_stack(chosen))

    return "{:.08f}".format(max(options) * math.pi)


SAMPLE = """
4
2 1
100 20
200 10
2 2
100 20
200 10
3 2
100 10
100 10
100 10
4 2
9 3
7 1
10 1
8 4
"""

if __name__ == "__main__":
    set_parsed_input(
        StringIO.StringIO(SAMPLE)
    )
    run_solver(solve)
