# -*- coding: utf-8 -*-
import sys

def flip_first_pancakes(field, size):
    assert(len(field) >= size)
    for i in range(size):
        if field[i] == "-":
            field[i] = "+"
        else:
            field[i] = "-"

def solve(question):
    field, size = question.split()
    size = int(size)
    field = [c for c in field]
    flip_count = 0
    while len(field) >= size:
        if field[0] == "-":
            flip_count += 1
            flip_first_pancakes(field, size)
        field = field[1:]
    if "-" in field:
        return "IMPOSSIBLE"
    return flip_count


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f_in, \
             open(sys.argv[1] + ".out", "w") as f_out:
        count = int(f_in.readline())
        for i in range(count):
            question = f_in.readline().strip()
            solution = solve(question)
            f_out.write("Case #%i: %s\n" % (i+1, str(solution)))
