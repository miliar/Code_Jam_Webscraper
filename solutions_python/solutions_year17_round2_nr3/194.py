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
    N, Q, cities, dist, neighbors, tasks = case_inputs
    cities = [None] + cities

    final_res = []
    for st, en in tasks:
        res = [None] + [defaultdict(lambda: MAX) for _ in range(N)]
        xp, sp = cities[st]
        res[st][(sp, xp)] = 0

        updated = True
        while updated:
            updated = False
            for src in range(1, N+1):
                for sp_xp, src_tm in res[src].items():
                    src_sp, src_xp = sp_xp
                    for dst, distance in neighbors[src].items():
                        if src_xp < distance - eps:
                            continue
                        dst_tm = src_tm + distance/src_sp

                        local_xp, local_sp = cities[dst]
                        if dst_tm < res[dst][(local_sp, local_xp)]:
                            updated = True
                            res[dst][(local_sp, local_xp)] = dst_tm

                        if src_xp - distance > 0 + eps:
                            dst_xp = src_xp - distance
                            if dst_tm < res[dst][(src_sp, dst_xp)]:
                                updated = True
                                res[dst][(src_sp, dst_xp)] = dst_tm
        # print(res[en].values())
        assert res[en].values()
        final_res.append(min(res[en].values()))
    return ' '.join(map(str, final_res))

################################################################################

def read_case(f):
    N, Q = read_ints(f)
    cities = [read_ints(f) for _ in range(N)]
    dist = [read_ints(f) for _ in range(N)]
    neighbors = defaultdict(dict)
    for src, line in enumerate(dist):
        for dst, d in enumerate(line):
            if d > -1:
                neighbors[src+1][dst+1] = d
    tasks = [read_ints(f) for _ in range(Q)]
    return N, Q, cities, dist, neighbors, tasks

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


