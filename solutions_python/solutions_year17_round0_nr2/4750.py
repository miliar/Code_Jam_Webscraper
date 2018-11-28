# Q1 of qual round
import pdb


class GcjBase(object):
    def __init__(self, debug_sol, no_of_lines_in_input):
        self.lines = None
        self.debug_sol = debug_sol
        self.case_no = 0
        self.no_of_lines_in_input = no_of_lines_in_input
        self.read_input_and_process()

    def debugger(self, msg):
        if self.debug_sol:
            print msg

    def print_sol(self, sol):
        print 'Case #{}: {}'.format(self.case_no, sol)

    def process_case(self):
        raise NotImplementedError

    def read_input_and_process(self):
        no_of_test_cases = int(raw_input())
        for self.case_no in xrange(1, no_of_test_cases + 1):
            self.debugger('case_no is ' + str(self.case_no))
            if self.no_of_lines_in_input == 1:
                self.lines = raw_input()
                self.process_case()
            else:
                self.lines = []
                for line_no in xrange(self.no_of_lines_in_input):
                    print line_no
                    self.lines.append(raw_input())
                self.process_case()


class Tidy(GcjBase):
    def process_case(self):
        no = self.lines
        """
            110 : 99 : 100 - 1
            223319: 223300 -1 :223299
                223000 -1 222999
            2110: 2000 - 1
            2118 : 2000 - 1
            11110 : 111109 : 1111
        """
        digits = len(no)
        mark = None
        t_mark = None
        for i in range(digits - 1):
            if ord(no[i]) == ord(no[i + 1]):
                if t_mark is None:
                    t_mark = i
            elif ord(no[i]) > ord(no[i + 1]):
                if t_mark is None:
                    mark = i
                else:
                    mark = t_mark
                break

        if mark is not None:
            no = no[:mark + 1] + '0' * (digits - (mark + 1))
            self.print_sol(int(no) - 1)
        else:
            self.print_sol(no)



Tidy(False, 1)
