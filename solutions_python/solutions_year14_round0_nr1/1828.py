#!/usr/bin/env python

import re
import sys

outf = 'out.txt'

class MagicTrick(object):

    def __init__(self, pid, fo):
        self.layout = [
                [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]],

                [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]]
        ]
        self.ans = [0, 0]
        self.pid = pid
        self.fo = fo

    def read_layout(self, q, r, rlo):
        """
        Parameters
        ----------
        q: int
            Question.

        r: int
            Row.

        rlo: list
            Row layout.
        """
        self.layout[q][r] = rlo

    def read_ans(self, q, a):
        self.ans[q] = a

    def poss_sol(self):
        sol = []
        for n in self.layout[1][self.ans[1]]:
            if n in self.layout[0][self.ans[0]]:
                sol.append(n)
        return sol

    def result(self, msg):
        string = "Case #" + str(self.pid) + ": " + msg
        return string

    def solve(self):
        sol = self.poss_sol()
        if len(sol) == 0:
            self.fo.write(self.result("Volunteer cheated!") + "\n")
        elif len(sol) == 1:
            self.fo.write(self.result(str(sol[0])) + "\n")
        else:
            self.fo.write(self.result("Bad magician!") + "\n")

    def test_print(self):
        for i in [0, 1]:
            print self.ans[i]
            for r in self.layout[i]:
                print r
        print ""


def read_and_solve(pid, fo):
    mto = MagicTrick(pid, fo)
    for i in range(2):
        # 0-based indexing
        mto.read_ans(i, int(raw_input()) - 1)
        for j in range(4):
            l = re.split(r'\s+', raw_input().strip())
            mto.read_layout(i, j, l)
    mto.solve()
    #mto.test_print()


def main():
    with open(outf, 'w') as fo:
        n = int(raw_input())
        ndone = 0
        while ndone < n:
            try:
                # 1-based numbering
                read_and_solve(ndone + 1, fo)
                ndone += 1
            except EOFError:
                break


if __name__ == "__main__":
    main()
