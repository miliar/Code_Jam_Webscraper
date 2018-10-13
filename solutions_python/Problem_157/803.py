from __future__ import print_function
from itertools import chain, cycle, islice, repeat
import sys

quat = {'1': {'1': '1', 'i': 'i', 'j': 'j', 'k': 'k'},
        'i': {'1': 'i', 'i': '-1', 'j': 'k', 'k': '-j'},
        'j': {'1': 'j', 'i': '-k', 'j': '-1', 'k': 'i'},
        'k': {'1': 'k', 'i': 'j', 'j': '-i', 'k': '-1'}}


def mul(a, b):
    if len(a) == len(b):
        sign = ''
    else:
        sign = '-'

    a_stripped = a[-1]
    b_stripped = b[-1]
    res = sign + quat[a_stripped][b_stripped]
    if len(res) == 3:
        res = res[-1]
    return res


def read_input(f):
    T = int(f.readline().strip())

    for i in xrange(T):
        output = {}
        line = f.readline().strip().split(" ")
        output['L'] = int(line[0])
        output['X'] = int(line[1])
        output['vals'] = f.readline().strip()
        yield output


def check_case(case):
    if len(set(list(case['vals']))) == 1:
        return "NO"

    max = case['L'] * case['X']

    vals = chain.from_iterable(repeat(list(case['vals']), case['X']))
    cur_i = '1'
    cur_j = '1'
    cur_k = '1'
    search_tree = {}

    for val in vals:
        cur_i = mul(cur_i, val)
        if cur_i == 'i':
            break

    for val in vals:
        cur_j = mul(cur_j, val)
        if cur_j == 'j':
            break

    for val in vals:
        cur_k = mul(cur_k, val)
    if cur_k == 'k' and cur_i == 'i' and cur_j == 'j':
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    input_filename = sys.argv[1]
    with open(input_filename) as input_file:
        case_no = 0
        for case in read_input(input_file):
            case_no += 1
            # check_case(case)
            print("Case #" + str(case_no) + ": " + check_case(case))
