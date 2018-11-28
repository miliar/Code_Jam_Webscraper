#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from base import GcjSolver

class WelcomeSolver(GcjSolver):
    magic = "welcome to code jam"

    def get_case(self):
        return self.get_line()
    def solve(self, case):
        self.count = 0
        self.check(case,0)
        return self.format(self.count)
    def check(self, line, index):
        if index == len(self.magic):
            self.count += 1
            return
        if len(line) == 0:
            return

        for i, c in enumerate(line):
            if c == self.magic[index]:
                self.check(line[i+1:], index+1)

    def format(self,n):
        s = str(n % 10000)
        if len(s) == 4:
            return s
        else:
            return "0"*(4-len(s)) + s
def main(program, name):
    s = WelcomeSolver(name)
    s.run()


if __name__ == '__main__':
    reload(sys); sys.setdefaultencoding('utf-8')
    main(*sys.argv)