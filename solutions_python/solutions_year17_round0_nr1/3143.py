from glob import glob
import numpy as np


def identical(a):
    return a


def convert_to_int(a):
    return [int(s) for s in a.split()]


def convert_to_float(a):
    return [float(s) for s in a.split()]


def convert_str_and_int(a):
    seq, n = a.split()
    pattern = np.array([s == '+' for s in seq], dtype=int)
    return [pattern, int(n)]


def parse_input(filename, translator):
    with open(filename, 'rb') as fp:
        input_data = fp.read().split('\n')
    n_case = int(input_data[0])
    data = [translator(s) for s in input_data[1:1+n_case]]
    return data


def solution(row):
    pattern, size = row
    count = 0
    for i in xrange(len(pattern) - size + 1):
        if pattern[i] == 0:
            count += 1
            pattern[i:i+size] = 1 - pattern[i:i+size]
    if pattern.sum() == len(pattern):
        return count
    return 'IMPOSSIBLE'


def prepare_output(data):
    result = []
    for i, row in enumerate(data):
        result.append('case #{}: {}'.format(i+1, solution(row)))
    return '\n'.join(result)


if __name__ == '__main__':
    input_files = glob('*.in')
    for in_file in input_files:
        outfile = '{}.out'.format(in_file.split('.')[0])
        result = prepare_output(parse_input(in_file, translator=convert_str_and_int))
        with open(outfile, 'wb') as fp:
            fp.write(result)
