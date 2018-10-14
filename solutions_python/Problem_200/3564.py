import os
import sys
import time

def is_tidy(number):
    _str = str(number)
    for i in xrange(len(_str)-1):
        if _str[i] > _str[i+1]:
            return False
    return True


def solve(line):
    number = int(line)
    for n in xrange(number, -1, -1):
        if is_tidy(n):
            return n


class Stopwatch(object):
    def __init__(self):
        self.start_ts = time.time()

    def end_and_print(self):
        print '{0}s'.format(time.time() - self.start_ts)


if __name__ == '__main__':
    stopwatch = Stopwatch()
    in_filename = sys.argv[1]
    out_filename = os.path.splitext(in_filename)[0] + '.out'
    with open(in_filename, 'r') as in_f, open(out_filename, 'w') as out_f:
        num_tests = int(in_f.readline())
        for idx, line in enumerate(in_f.readlines()):
            result = 'Case #{0}: {1}'.format(idx + 1, solve(line))
            print result
            out_f.write(result + '\n')
    stopwatch.end_and_print()