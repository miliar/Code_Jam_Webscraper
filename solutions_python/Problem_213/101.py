import heapq
import sys
import math
from collections import defaultdict
from itertools import product
from multiprocessing.pool import Pool

from sortedcontainers import sorteddict
from tqdm import tqdm

################################################################################

CONCURRENCY = 0

eps = 10e-7
MAX = 999999999999999999


def solve(case_inputs):
    N, C, M, pbs = case_inputs

    c_bought = [0] * (C+1)
    p_bought = [0] * (N+1)

    for p, b in pbs:
        p_bought[p] += 1
        c_bought[b] += 1

    train_no = 0
    sm = 0
    for i in range(1, N+1):
        sm += p_bought[i]
        train_no = max(train_no, math.ceil(sm/i))
    train_no = max(train_no, max(c_bought))

    left = 0
    res = 0
    for i in range(1, N+1):
        bo = p_bought[i]
        if bo > train_no:
            d = bo - train_no
            res += d
            left -= d
        elif bo < train_no:
            d = train_no - bo
            left += d
        else:
            pass
        assert left >= 0

    return ' '.join([str(train_no), str(res)])

################################################################################

def read_case(f):
    N, C, M = read_ints(f)
    pbs = [read_ints(f) for _ in range(M)]
    return N, C, M, pbs

def write_case(f, i, res):
    f.write('Case #%s: '%i)
    f.write('%s'%res)
    f.write('\n')

################################################################################

def read_word(f):
    return next(f).strip()

def read_int(f, b=10):
    return int(read_word(f), b)

def read_letters(f):
    return list(read_word(f))

def read_digits(f, b=10):
    return [int(x, b) for x in read_letters(f)]

def read_words(f, d=' '):
    return read_word(f).split(d)

def read_ints(f, b=10, d=' '):
    return [int(x, b) for x in read_words(f, d)]

def read_floats(f, d=' '):
    return [float(x) for x in read_words(f, d)]

def read_arr(f, R, reader=read_ints, *args, **kwargs):
    return [reader(f, *args, **kwargs) for i in range(R)]

def out_file(in_file):
    return in_file[:in_file.rfind('.')] + '.out'

def main():
    if len(sys.argv) != 2:
        print('usage: python <file_name> <input_file>')
        sys.exit(1)

    with open(sys.argv[1], 'r') as f, open(out_file(sys.argv[1]), 'w') as w:
        count = read_int(f)
        if CONCURRENCY > 0:
            solve_concurrent(CONCURRENCY, count, f, w)
        else:
            solve_single_process(count, f, w)

def solve_concurrent(CONCURRENCY, count, f, w):
    problems = [read_case(f) for _ in range(count)]
    with Pool(CONCURRENCY) as p:
        solutions = p.map(solve, problems)
    assert len(solutions) == count
    for i in tqdm(range(count), desc='[** CONCURRENCY={} **] Writing solutions to output file'.format(CONCURRENCY)):
        write_case(w, i + 1, solutions[i])

def solve_single_process(count, f, w):
    for i in tqdm(range(1, count + 1), desc='Solving problems and writing solutions to output file'):
        case_inputs = read_case(f)
        write_case(w, i, solve(case_inputs))


if __name__ == "__main__":
    main()


