# -*- coding: utf-8 -*-

from base import CodeJamBase
import sys

__author__ = "Evan"

class MagicTrick(CodeJamBase):

    def _collect_args(self):
        self.row_answer_1 = self._read_line_as_list().pop()
        self.arr1 = []
        self.arr1.append( self._read_line_as_list() )
        self.arr1.append( self._read_line_as_list() )
        self.arr1.append( self._read_line_as_list() )
        self.arr1.append( self._read_line_as_list() )
        self.row_answer_2 = self._read_line_as_list().pop()
        self.arr2 = []
        self.arr2.append( self._read_line_as_list() )
        self.arr2.append( self._read_line_as_list() )
        self.arr2.append( self._read_line_as_list() )
        self.arr2.append( self._read_line_as_list() )
        

    def _test(self):
        options1 = set(self.arr1[int(self.row_answer_1) - 1])
        options2 = set(self.arr2[int(self.row_answer_2) - 1])

        sol = options1.intersection(options2)

        # print sol
        if len(sol) == 1:
            ret = str(sol.pop())
        elif len(sol) == 0:
            ret = "Volunteer cheated!"
        else:
            ret = "Bad magician!"

        print ret        

        return [ret]

def main():
    """
    copy this into any actual challenge solcing code
    """
    sim = MagicTrick()
    sim.run_tests(sys.argv[1])

if __name__ == "__main__":
    main()