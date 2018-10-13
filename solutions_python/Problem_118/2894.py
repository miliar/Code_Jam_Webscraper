import sys
import math

class FairAndSquare(object):

    def __init__(self, input_fn):
        self.input_filename = input_fn
        self.output_filename = 'results.txt'
        
        self.input = open(self.input_filename, 'r')
        self.output = open(self.output_filename, 'a')

    def process(self):
        test_cases = int(self.input.readline()) + 1
        for i in xrange(1, test_cases):
            self.readin_interval(i)

    def readin_interval(self, case_num):
        interval = self.input.readline().rstrip('\n').split()
        count = 0
        min = int(interval[0])
        max = int(interval[1]) + 1
        for i in xrange(min, max):
            ispalin = self.is_palindrome(i)
            if ispalin:
                sq_rt = math.sqrt(i)
                if math.modf(sq_rt)[0] == 0.0:
                    sq_palin = self.is_palindrome(int(sq_rt))
                    if sq_palin:
                        count += 1
        self.print_result(case_num, count)

    def print_result(self, case_num, count):
        self.output.write('Case #%s: %s\n' % (str(case_num), str(count)))

    def is_palindrome(self, i):
        int_str = str(i)
        length = len(int_str)
        if length == 1:
            return True
        ind_len = length - 1
        for i in xrange(length / 2):
            if int_str[i] != int_str[ind_len - i]:
                return False
        return True

if __name__ == '__main__':
    INPUT_FILENAME = sys.argv[1]
    tester = FairAndSquare(INPUT_FILENAME)
    tester.process()
