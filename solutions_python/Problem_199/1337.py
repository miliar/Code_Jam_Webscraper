import sys
import math
from multiprocessing.pool import Pool

from tqdm import tqdm

################################################################################

CONCURRENCY = 0

eps = 10e-6


def solve(case_inputs):
    n, orig_pans = case_inputs

    pans = list(orig_pans)
    cnt1 = 0
    for i in range(len(pans)-n+1):

        if not pans[i]:
            cnt1 += 1
            for j in range(i, i+n):
                pans[j] = not pans[j]

    if not all(pans):
        cnt1 = 10e20

    pans = list(orig_pans)[::-1]
    cnt2 = 0
    for i in range(len(pans) - n + 1):
        if not pans[i]:
            cnt2 += 1
            for j in range(i, i + n):
                pans[j] = not pans[j]

    if not all(pans):
        cnt2 = 10e20

    if min(cnt1, cnt2) < 10e20:
        return str(min(cnt1, cnt2))
    return 'IMPOSSIBLE'


################################################################################

def read_case(f):
    pan, n = read_words(f)
    d = {'-': False, '+': True}
    return int(n), list(map(d.__getitem__, pan))

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


