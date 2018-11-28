from itertools import product, combinations

import collections

from collections import defaultdict, Counter

import heapq
import sys
import math
from multiprocessing.pool import Pool

from sortedcontainers import SortedDict
from tqdm import tqdm

################################################################################

CONCURRENCY = 0

eps = 1e-7
MAX = 999999999999999999

def solve(case_inputs):
    cs, js = case_inputs
    c2 = [(c, 'c') for c in cs]
    l_c = 60*12 - sum([d-c for c, d in cs])

    j2 = [(j, 'j') for j in js]
    l_j = 60*12 - sum([d - c for c, d in js])
    both = sorted(c2 + j2)

    diffs = []
    for i in range(len(both)):
        inte1, p1 = both[i]
        inte2, p2 = both[(i+1)%len(both)]
        _, d1 = inte1
        c2, _ = inte2
        delta = (c2-d1) % (60*24)
        diffs.append((delta, i))

    diffs.sort()
    swaps = 0
    for delta, i in diffs:
        inte1, p1 = both[i]
        inte2, p2 = both[(i + 1) % len(both)]
        if p1 == p2:
            if p1 == 'c' and l_c - delta >= 0 - eps:
                l_c -= delta
            elif p1 == 'j' and l_j - delta >= 0 - eps:
                l_j -= delta
            else:
                swaps += 2
        else:
            swaps += 1

    return swaps

################################################################################

def read_case(f):
    Ac, Aj = read_ints(f)
    cs = [read_ints(f) for _ in range(Ac)]
    js = [read_ints(f) for _ in range(Aj)]
    return cs, js

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
        print(i)
        case_inputs = read_case(f)
        write_case(w, i, solve(case_inputs))


if __name__ == "__main__":
    main()


