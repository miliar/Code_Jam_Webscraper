# Q1 of qual round
import pdb

import math


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
            if self.no_of_lines_in_input == 1:
                self.lines = raw_input()
            else:
                self.lines = []
                for line_no in xrange(self.no_of_lines_in_input):
                    self.lines.append(raw_input())
            self.debugger('case_no ' + str(self.case_no) + 'i/p : ' + str(self.lines))
            self.process_case()



class Bathroom(GcjBase):

    
    def process_case(self):
        def find_max(booths):
            max_booth = 0
            max_i = 0
            for i, booth in enumerate(booths):
                if booth > max_booth:
                    max_booth = booth
                    max_i = i
            return max_booth, max_i
        booths, persons = self.lines.split(' ')
        booths = float(booths)
        persons = int(persons)
        if persons == booths:
            self.print_sol('%d %d' % (0, 0))
            return
        # import pdb
        # pdb.set_trace()
        booth_seq = [booths, ]
        ls, rs = 0, 0
        for person in range(persons):
            c, ci = find_max(booth_seq)
            sel = math.ceil(c/2)
            temp_booth_seq = []
            ls = sel - 1
            rs = c - sel
            if person+1 != persons or self.debug_sol:
                for bi, booth in enumerate(booth_seq):
                    if bi != ci:
                        temp_booth_seq.append(booth)
                    else:
                        if ls:
                            temp_booth_seq.append(ls)
                        if rs:
                            temp_booth_seq.append(rs)
                booth_seq = temp_booth_seq
                # self.debugger("state of debugger %s")
        # import pdb; pdb.set_trace()
        self.print_sol('%d %d' % (max(ls, rs), min(ls, rs)))


Bathroom(False, 1)