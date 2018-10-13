# -*- coding: utf-8 -*-

import unittest
import sys


def solve_problem(public):
    friends = 0
    clapping = 0

    for i in range(len(public)):
        p = int(public[i])
        if p > 0 and i > (clapping + friends):
            friends += i - (clapping + friends)
        clapping += p
    return friends


class ProblemTest(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(solve_problem("11111"), 0)
        self.assertEqual(solve_problem("09"), 1)
        self.assertEqual(solve_problem("110011"), 2)
        self.assertEqual(solve_problem("1"), 0)
        self.assertEqual(solve_problem("11111111"), 0)
        self.assertEqual(solve_problem("10000001"), 6)
        self.assertEqual(solve_problem("40000001"), 3)
        self.assertEqual(solve_problem("10201"), 1)
        self.assertEqual(solve_problem("4101"), 0)

def main():
    fin = open(sys.argv[1])
    fout = open(sys.argv[2], 'w')

    index = 1
    for l in fin.readlines()[1:]:
        public = l.split(" ")[1].strip()
        r = solve_problem(public)
        fout.write("Case #{}: {}\n".format(index, r))
        index += 1

    fout.close()
    fin.close()

if __name__ == '__main__':
    main()
