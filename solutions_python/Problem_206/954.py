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
    data = [translator(s) for s in input_data[1:]]
    return n_case, data


def solution(tot_dist, horses):
    horses.sort(key=lambda s: (-s[0], s[1]))
    travel_time = 0
    for hs in horses:
        travel_time = max((tot_dist - hs[0]) / hs[1], travel_time)
    return tot_dist / travel_time


def prepare_output(content):
    n_case, data = content
    result = []
    r_idx = 0
    for i in xrange(n_case):
        annie = data[r_idx]
        other_horses = data[r_idx+1: r_idx+1+int(annie[1])]
        travel_speed = solution(annie[0], other_horses)
        result.append('case #{}: {}'.format(i+1, travel_speed))
        r_idx += int(annie[1]) + 1
    return '\n'.join(result)


if __name__ == '__main__':
    input_files = glob('*.in')
    for in_file in input_files:
        outfile = '{}.out'.format(in_file.split('.')[0])
        result = prepare_output(parse_input(in_file, translator=convert_to_float))
        with open(outfile, 'wb') as fp:
            fp.write(result)
