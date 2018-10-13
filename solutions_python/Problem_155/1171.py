from __future__ import print_function
import sys


def read_input(f):
    T = int(f.readline().strip())

    for i in xrange(T):
        output = {}
        line = f.readline().strip().split(" ")
        output['smax'] = int(line[0])
        output['vals'] = [int(x) for x in line[1]]
        yield output


def check_case(case):
    smax = case['smax']
    vals = case['vals']
    invited = 0
    acc = 0

    for shyness, val in enumerate(vals):
        if shyness > smax:
            break
        # check to see if we have more than enough people to reach the
        # shyness level
        diff = shyness - (acc + invited)
        if diff > 0:
            # invite more at this level to reach shyness
            invited = invited + diff
        # add the people at this level to the accumulator
        acc = acc + val

    return str(invited)


if __name__ == "__main__":
    input_filename  = sys.argv[1]
    with open(input_filename) as input_file:
        case_no = 0
        for case in read_input(input_file):
            case_no += 1
            # check_case(case)
            print("Case #" + str(case_no) + ": " + check_case(case))
