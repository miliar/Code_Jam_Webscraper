#!/usr/bin/env python

import numpy as np
import sys


def write_output_line(f, case, result):
    assert result in ('RICHARD', 'GABRIEL')
    f.write('Case #{}: {}\n'.format(case, result))


# 1-ominos
#   X
#
# 2-ominos
#   XX
#
# 3-ominos
#   X  XX
#   X   X
#   X
#
# 4-ominos
#   X  XXX  XX   XX  XXX
#   X    X   XX  XX   X
#   X
#   X


def classify(arrs, idxs=None):
    def to_ij(grid):
        idxs = list(zip(*np.where(grid)))
        mini = min(i for i, j in idxs)
        minj = min(j for i, j in idxs)
        return [(i - mini, j - minj) for i, j in idxs]

    classified_idxs = [] if idxs is None else idxs
    classifications = []
    transformations = [
        (),
        (np.rot90,),
        (np.rot90, np.rot90),
        (np.rot90, np.rot90, np.rot90),
        (np.fliplr,),
        (np.flipud,),
    ]

    for arr in arrs:
        classification = -1

        for fs in transformations:
            grid = arr.copy()

            for f in fs:
                grid = f(grid)

            idxs = to_ij(grid)

            if idxs in classified_idxs:
                classification = classified_idxs.index(idxs)
                break

        if classification == -1:
            classified_idxs.append(idxs)
            classification = classified_idxs.index(idxs)

        classifications.append(classification)

    return classified_idxs, classifications


class OminoGrid():
    def __init__(self, X, R, C):
        self.grid = np.zeros((R, C), dtype=np.bool)
        self.X = X
        self.R = R
        self.C = C

    @property
    def is_solved(self):
        return self.grid.all()

    def iter_place(self, i, j, n=None):
        if n is None:
            n = self.X

        if self.grid[i, j]:
            return

        backup = self.grid.copy()
        self.grid[i, j] = True

        if n == 1:
            yield self.grid  # base case
        else:
            deltas = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # four points

            for di, dj in deltas:
                ni = i + di
                nj = j + dj

                if ni < 0 or ni >= self.R or nj < 0 or nj >= self.C:
                    continue

                for grid in self.iter_place(ni, nj, n=n - 1):
                    yield grid

        self.grid = backup

    def can_solve(self):
        if self.is_solved:
            return True

        empty_places = np.where(self.grid == False)
        for i, j in zip(*empty_places):
            for grid in self.iter_place(i, j):
                backup = self.grid.copy()
                self.grid = grid

                if self.can_solve():
                    return True

                self.grid = backup

        return False

    def can_solve_all(self):
        # get unique idxs
        # pretend to be a massive grid first so we get all possibilities
        backup, R, C = self.grid.copy(), self.R, self.C
        self.grid = np.zeros((20, 20), dtype=np.bool)
        self.R = 20
        self.C = 20

        classified_idxs, all_classifications = classify(self.iter_place(0, 0))
        self.grid, self.R, self.C = backup, R, C

        # if every index has solved att at least one point, we're ok
        has_solved = {i: False for i in all_classifications}

        for i, j in ((i, j) for i in range(self.R) for j in range(self.C)):
            for grid in self.iter_place(i, j):
                idxs, classifications = classify([grid], idxs=classified_idxs)
                assert idxs == classified_idxs

                classification = classifications[0]
                if classification not in has_solved or has_solved[classification]:
                    continue

                backup = self.grid.copy()
                self.grid = grid

                if self.can_solve():
                    has_solved[classification] = True

                self.grid = backup

                if all(has_solved.values()):
                    break
            if all(has_solved.values()):
                break

        return all(has_solved.values())


def main(input_path, output_path):
    with open(input_path) as f_in, open(output_path, 'w') as f_out:
        f_in.readline()  # number of cases

        for n, line in enumerate(f_in):
            if not line.strip():
                continue

            X, R, C = map(int, line.split())

            # some X-ominos will be an auto-win
            # 1-omino: GABRIEL (can fill any grid)
            # 7-omino: RICHARD (has hole)
            #   xxx
            #   x x
            #   xx
            # 8-omino and above: RICHARD (same logic)
            #
            # also, any X > R and X > C is a win, as you can pick the long one
            # also, any X//2 - X%2 > min(R, C) is a win as the short L extrudes
            # also, any number of squares which are not evenly divisible by X
            if X == 1:
                winner = 'GABRIEL'
            elif X >= 7 \
                    or (X > R and X > C) \
                    or X//2 + X%2 > min([R, C]) \
                    or (R*C)%X != 0:
                winner = 'RICHARD'
            else:  # no shortcut here
                if OminoGrid(X, R, C).can_solve_all():
                    winner = 'GABRIEL'
                else:
                    winner = 'RICHARD'

            write_output_line(f_out, n + 1, winner)


if __name__ == '__main__':
    if not sys.argv[2:]:
        sys.argv.append(sys.argv[1].replace('in', 'out'))

    main(sys.argv[1], sys.argv[2])
