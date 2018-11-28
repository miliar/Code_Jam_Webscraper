import heapq
import sys
import math
from multiprocessing.pool import Pool

from tqdm import tqdm

################################################################################

CONCURRENCY = 7

eps = 10e-6


def solve(case_inputs):
    n, k = case_inputs
    # print(n, k)

    heap = [(-n, 0)]
    heapq.heapify(heap)
    for _ in range(k-1):
        length, pos = heapq.heappop(heap)
        length *= -1
        if length == 1:
            continue
        if length == 2:
            heapq.heappush(heap, (-1, pos+1))
        else:
            chosen_pos = pos + (length-1)//2
            heapq.heappush(heap, (-(chosen_pos-pos), pos))
            heapq.heappush(heap, (-(pos+length-chosen_pos-1), chosen_pos+1))

    length, pos = heapq.heappop(heap)
    length *= -1
    # print(heap)
    # print(length, pos)

    chosen_pos = pos + (length-1) // 2
    l = chosen_pos-pos
    r = pos+length-chosen_pos-1
    y = max(l, r)
    x = min(l, r)
    return "{} {}".format(y, x)


################################################################################

def read_case(f):
    return read_ints(f)

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


