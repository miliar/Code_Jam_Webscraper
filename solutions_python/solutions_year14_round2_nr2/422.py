from __future__ import print_function
import sys


def read_input(f):
    T = int(f.readline().strip())

    for i in xrange(T):
        A, B, K = [int(val) for val in f.readline().strip().split(" ")]
        yield (A, B, K)


def check_case(case):
    A, B, K = case
    acc = 0
    for a in xrange(A):
        for b in xrange(B):
            if a & b < K:
                acc += 1
    return str(acc)


if __name__ == "__main__":
    input_filename = sys.argv[1]
    with open(input_filename) as input_file:
        case_no = 0
        for case in read_input(input_file):
            case_no += 1
            # check_case(case)
            print("Case #" + str(case_no) + ": " + check_case(case))
