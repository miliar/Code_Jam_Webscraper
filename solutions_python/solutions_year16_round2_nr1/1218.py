import sys

class GcjBase(object):

    def __init__(self, debug_sol, no_of_lines_in_input ):
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
        for self.case_no in xrange(1, no_of_test_cases+1):
            self.debugger('case_no is ' + str(self.case_no))
            if self.no_of_lines_in_input ==1:
                self.lines = raw_input()
                self.process_case()
            else:
                self.lines = []
                for line_no in xrange(self.no_of_lines_in_input):
                    print line_no
                    self.lines.append(raw_input())
                self.process_case()



class A(GcjBase):

    def process_case(self):
        z = w = u =  x= g=  o=  r= f=  s=  I = 0

        for ch in self.lines:
            if ch == 'Z':
                z += 1
            elif ch == 'W':
                w += 1
            elif ch == 'U':
                u += 1
            elif ch == 'X':
                x += 1
            elif ch == 'G':
                g += 1
            elif ch == 'O':
                o += 1
            elif ch == 'R':
                r += 1
            elif ch == 'S':
                s += 1
            elif ch == 'F':
                f += 1
            elif ch == 'I':
                I += 1

        if self.debug_sol:
            print "z {} w {} u {}  x {} g {}  o {}  r{} f{}  s{}  i{}".format(z , w , u ,  x, g,  o,  r, f,  s,  I)
            print I-f+u-x-g

        sol = ''
        for i in xrange(z):
            sol += '0'
        for i in xrange(o-w-u-z):
            sol += '1'
        for i in xrange(w):
            sol += '2'
        for i in xrange(r-z-u):
            sol += '3'
        for i in xrange(u):
            sol += '4'
        for i in xrange(f-u):
            sol += '5'

        for i in xrange(x):
            sol += '6'
        for i in xrange(s-x):
            sol += '7'
        for i in xrange(g):
            sol += '8'

        for i in range(I-f+u-x-g):
            sol += '9'

        self.print_sol(sol)

a = A(False, 1)
