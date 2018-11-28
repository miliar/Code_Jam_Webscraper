from __future__ import print_function
import sys


def read_input(f):
    T = int(f.readline().strip())

    for i in xrange(T):
        N = int(f.readline().strip())
        strings = [f.readline().strip() for j in xrange(N)]
        yield strings


def canonize(s):
    result = []
    cur = s[0]
    cur_count = 1
    for i in range(1, len(s)):
        if cur == s[i]:
            cur_count += 1
        else:
            result.append((cur, cur_count))
            cur = s[i]
            cur_count = 1
    result.append((cur, cur_count))
    return result


def flatten_canonized(string):
    return ''.join(val[0] for val in string)


def check_case(case):
    # check to see if the strings match in pattern of characters by
    # canonizing into pairs of char, count
    runs = [canonize(s) for s in case]

    flattened = [flatten_canonized(val) for val in runs]

    if not(all([flattened[0] == flattened[i]
                for i in xrange(1, len(flattened))])):
        return "Fegla Won"

    def get_counts(index):
        return [run[index][1] for run in runs]

    # figure out minimum number of moves to make them identical
    # compute the mean and round to the nearest integer. take
    # differences between each value and the mean. Sum moves.
    acc = 0
    for i in xrange(len(runs[0])):
        counts = get_counts(i)
        mean = int(round(float(sum(counts)) / float(len(counts))))
        diffs = [abs(mean - count) for count in counts]
        acc += sum(diffs)

    return str(acc)


if __name__ == "__main__":
    input_filename = sys.argv[1]
    with open(input_filename) as input_file:
        case_no = 0
        for case in read_input(input_file):
            case_no += 1
            # check_case(case)
            print("Case #" + str(case_no) + ": " + check_case(case))
