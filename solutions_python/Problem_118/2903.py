import os
import sys
import re
import math

abpath = lambda x: os.path.abspath(os.path.join(os.path.dirname(__file__), x))


class Fair(object):
    def __init__(self, in_fh, out_fh):
        self.num_cases = int(in_fh.readline())
        self.in_fh = in_fh
        self.out_fh = out_fh

    def solve_all(self):
        for i in range(self.num_cases):
            case = self.in_fh.readline().strip()
            int_range = [int(s) for s in case.split() if s.isdigit()]
            from_int = int_range[0]
            to_int = int_range[1]
            answer = self.solve_case(from_int, to_int)
            line_output = ''.join(('Case #', str(i + 1),
                                   ': ', str(answer), '\n'))
            self.out_fh.write(line_output)

    def solve_case(self, from_int, to_int):
        fas_count = 0
        for integer in range(from_int, to_int+1):
            if self.is_palindrome(integer):
                is_fas = self.is_palindrome(math.sqrt(integer))
                if is_fas:
                    fas_count += 1
        return fas_count

    def is_palindrome(self, number):
        num_string = str(number)
        num_string = re.sub(r'.0$', '', num_string)
        reverse_num_string = num_string[::-1]
        outcome = False
        if num_string == reverse_num_string:
            outcome = True
        return outcome


def main():
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    in_path = abpath('input/' + in_file)
    out_path = abpath('output/' + out_file)
    with open(in_path, 'r') as in_fh, open(out_path, 'w+') as out_fh:
        fair = Fair(in_fh, out_fh)
        fair.solve_all()

if __name__ == '__main__':
    main()
