import sys
import math
from itertools import product
from multiprocessing.pool import Pool

from tqdm import tqdm

################################################################################

CONCURRENCY = 0

eps = 10e-6

def get_max(R, Y, B):
    if R == Y == B == 0:
        return None

    if R >= max(Y, B):
        return 'R'
    elif Y >= B:
        return 'Y'
    else:
        return 'B'


def solve(case_inputs):
    # print('start')
    N, R, O, Y, G, B, V = case_inputs
    res = []
    last = None
    for i in range(N):
        if not last:
            mx = get_max(R, Y, B)
            res.append(mx)
            if mx == 'R':
                R -= 1
            elif mx == 'Y':
                Y -= 1
            elif mx == 'B':
                B -= 1
            else:
                assert False
            last = mx
            continue

        r, y, b = R, Y, B
        if last == 'R':
            r = 0
        elif last == 'Y':
            y = 0
        elif last == 'B':
            b = 0
        else:
            raise Exception ('unknown last {}'.format(last))
        mx = get_max(r, y, b)
        if not mx:
            return 'IMPOSSIBLE'
        else:
            if mx == 'R':
                R -= 1
            elif mx == 'Y':
                Y -= 1
            elif mx == 'B':
                B -= 1
            else:
                assert False
            last = mx
            res.append(mx)


    # print(res)
    if res[0] == res[-1]:
        if res[0] == res[-3]:
            return 'IMPOSSIBLE'
        else:
            res[-1] = res[-2]
            res[-2] = res[0]

    # check
    last = res[-1]
    for i in range(N):
        assert res[i] != last
        last = res[i]

    return ''.join(res)


################################################################################

def read_case(f):
    N, R, O, Y, G, B, V = read_ints(f)
    return N, R, O, Y, G, B, V

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


