import StringIO
import random
from collections import OrderedDict

from ecodejam.input_parser import read_int, set_parsed_input, run_solver


def is_legal(res):
    for a, b in zip(res, res[1:] + res[:1]):
        if a == b:
            return False
    return True


def solve_small(case_index):
    n = read_int()

    r = read_int()
    o = read_int()
    y = read_int()
    g = read_int()
    b = read_int()
    v = read_int()

    assert o == 0
    assert v == 0
    assert g == 0

    colors = OrderedDict([
        ("R", r),
        ("O", o),
        ("Y", y),
        ("G", g),
        ("B", b),
        ("V", v),
    ])

    if r > y + b or y > r + b or b > y + r:
        return "IMPOSSIBLE"

    ret = ""
    forbidden = None

    for i in xrange(n):
        temp_colors = OrderedDict(colors)

        if forbidden is not None:
            temp_colors.pop(forbidden)

        next_col = max(temp_colors.items(), key=lambda x: x[1])[0]
        colors[next_col] -= 1
        forbidden = next_col
        ret += next_col

    print ret

    for i in xrange(1000):
        if is_legal(ret):
            break
        l = list(ret[-5:])
        random.shuffle(l)
        ret = ret[:-5] + "".join(l)

    if not is_legal(ret):
        raise Exception("Not legal!!")

    return ret

solve = solve_small

SAMPLE = """
3
6 2 0 2 0 2 0
3 1 0 2 0 0 0
10 5 0 2 0 3 0
"""

if __name__ == "__main__":
    set_parsed_input(
        StringIO.StringIO(SAMPLE)
    )
    run_solver(solve)
