# -*- coding: utf-8 -*-

import unittest
import sys


def solve_problem(X, R, C):
    if X == 1:
        return "GABRIEL"

    # x-omnio with hole inside is possible
    if X >= 7:
        return "RICHARD"

    # straight x-omnio bigger than grid
    if X > max(R, C):
        return "RICHARD"

    # impossible to exaclty fill grid with x-omnios
    if (R * C) % X != 0:
        return "RICHARD"

    # L shaped x-omnio won't fit grid
    if X % 2 == 1 and min(R, C) < (X // 2 + 1):
        return "RICHARD"
    if X % 2 == 0 and min(R, C) < (X // 2):
        return "RICHARD"

    # Richar always win with S shaped 4-omnio in 2x4 grid
    if X == 4 and 2 in [R, C] and 4 in [R, C]:
        return "RICHARD"

    return "GABRIEL"


class ProblemTest(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(solve_problem(2, 2, 2), "GABRIEL")
        self.assertEqual(solve_problem(2, 1, 3), "RICHARD")
        self.assertEqual(solve_problem(4, 4, 1), "RICHARD")
        self.assertEqual(solve_problem(3, 2, 3), "GABRIEL")
        self.assertEqual(solve_problem(7, 100, 100), "RICHARD")
        self.assertEqual(solve_problem(3, 10, 1), "RICHARD")
        self.assertEqual(solve_problem(5, 2, 5), "RICHARD")
        self.assertEqual(solve_problem(6, 2, 5), "RICHARD")
        self.assertEqual(solve_problem(1, 1, 2), "GABRIEL")
        self.assertEqual(solve_problem(3, 4, 1), "RICHARD")
        self.assertEqual(solve_problem(2, 1, 4), "GABRIEL")
        self.assertEqual(solve_problem(4, 4, 2), "RICHARD")


def main():
    fin = open(sys.argv[1])
    fout = open(sys.argv[2], 'w')

    index = 1
    for l in fin.readlines()[1:]:
        X, R, C = [int(n.strip()) for n in l.split(" ")]
        r = solve_problem(X, R, C)
        fout.write("Case #{}: {}\n".format(index, r))
        index += 1

    fout.close()
    fin.close()

if __name__ == '__main__':
    main()
