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
    result = []
    initial_len = len(row)
    for i, s in enumerate(row):
        si = int(s)
        if result and si < result[-1]:
            result = process(result)
            result.extend([9] * (initial_len - i))
            break
        else:
            result.append(si)
    ret = int(''.join([str(s) for s in result]))
    print '{} -> {}'.format(row, ret)
    return ret


def process(result):
    m = result[-1]
    for i in xrange(len(result) - 1, 0, -1):
        result[i] -= 1
        if result[i] >= result[i-1]:
            return result
        else:
            result[i] = 9
    if result[0] == 1:
        return [9] * (len(result) - 1)
    else:
        result[0] -= 1
        return result


def prepare_output(data):
    result = []
    for i, row in enumerate(data):
        result.append('case #{}: {}'.format(i+1, solution(row)))
    return '\n'.join(result)


if __name__ == '__main__':
    # solution('110')
    input_files = glob('*.in')
    for in_file in input_files:
        outfile = '{}.out'.format(in_file.split('.')[0])
        result = prepare_output(parse_input(in_file, translator=identical))
        with open(outfile, 'wb') as fp:
            fp.write(result)
