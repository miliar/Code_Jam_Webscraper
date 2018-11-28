#!/usr/bin/env python3

"""Problem A (large): Oversized Pancake Flipper."""

import re


def sort(row, fliper_length):
    index = row.find("-")

    # Full happy side up
    if index < 0:
        return 0

    else:
        result = 1

        while index + fliper_length <= len(row):
            limit = index + fliper_length
            row = flip(row[index:limit]) + row[limit:]
            index = row.find("-")

            if "-" not in row:
                return result

            result += 1

        return "IMPOSSIBLE"


def flip(portion):
    return "".join(["+" if side == "-" else "-" for side in portion])


pattern = re.compile(r"^[+-]+$")
out = open("A-large.out", "w")

with open("A-large.in") as in_file:
    T = int(in_file.readline())

    assert 1 <= T <= 100

    for case in range(1, T + 1):
        S, K = in_file.readline().split()
        K = int(K)
        len_S = len(S)

        assert 2 <= len_S <= 1000
        # Every character in S is either + or -
        assert pattern.match(S)
        assert 2 <= K <= len_S

        result = sort(S, K)

        out.write("Case #{}: {}\n".format(case, result))
