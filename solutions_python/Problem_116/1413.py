#!/usr/bin/env python
import sys, os
from inspect import getargspec

class Break(Exception): pass
class IntList: pass
class StrList: pass

class ProblemBase(object):
    def __init__(self, fh):
        self._fh = fh
        aspec = getargspec(self.run_case)
        self.varvalts = zip(aspec.args[1:], aspec.defaults)

    def get_str(self):
        return self._fh.readline().strip()
    def get_int(self):
        return int(self.get_str())
    def get_strlist(self):
        return self.get_str().split()
    def get_intlist(self):
        return map(int, self.get_strlist())

    def print_result(self, case_no, result):
        print "Case #%i: %s" % (case_no, str(result))

    def run(self):
        self.N = self.get_int()
        for n in range(1, self.N+1):
            self._run_case(n)

    def _run_case(self, case_no):
        kw = {}
        for var, val in self.varvalts:
            if val == int:
                kw[var] = self.get_int()
            elif val == str:
                kw[var] = self.get_str()
            elif val == IntList:
                kw[var] = self.get_intlist()
            elif val == StrList:
                kw[var] = self.get_strlist()
            else:
                raise RuntimeError("Unknown method args specified on run_case method")

        self.print_result(case_no, self.run_case(**kw))


import re
Pline = re.compile(r'.*\..*')
Xline = re.compile(r'[XT]{4}')
Oline = re.compile(r'[OT]{4}')
class ProblemCase(ProblemBase):
    def run_case(self,
                 r1=str, r2=str, r3=str, r4=str, _=str):
        lines = \
            [r1, r2, r3, r4] + \
            [''.join(c) for c in zip(r1,r2,r3,r4)] + \
            [''.join((r1[0], r2[1], r3[2], r4[3])),
             ''.join((r1[3], r2[2], r3[1], r4[0]))]

        for L in lines:
            if Xline.match(L): return "X won"
            if Oline.match(L): return "O won"

        for L in lines:
            if Pline.match(L): return "Game has not completed"

        return "Draw"


if __name__ == '__main__':

    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        cases = ProblemCase(open(sys.argv[1]))
    else:
        cases = ProblemCase(sys.stdin)

    cases.run()
