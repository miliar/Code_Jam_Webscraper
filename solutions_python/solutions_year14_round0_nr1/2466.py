#!/usr/bin/env python
import fileinput

N_GRIDS = 2
N_ROWS = 4
N_CARDS = 16

if __name__ == "__main__":
    lines = fileinput.input()

    n_cases = int(lines.readline())

    for case in range(n_cases):
        solutions = set(range(1, N_CARDS + 1))
        for grid in range(N_GRIDS):
            choice = int(lines.readline());
            for row in range(N_ROWS):
                cards = [int(i) for i in lines.readline().split()]
                if row == choice - 1:
                    solutions = solutions & set(cards)
        size = len(solutions)
        if size == 0:
            msg = "Volunteer cheated!"
        elif size == 1:
            msg = solutions.pop()
        else:
            msg = "Bad magician!"

        print("Case #{}: {}".format(case + 1, msg))
