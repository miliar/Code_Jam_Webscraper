#!/etc/env/python python
import argparse

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

def solve(solver, fn, out_fn=None):
    in_fn = fn + '.in'
    #if out_fn is None:
    out_fn = fn + '.out'
    with open(in_fn, 'r') as fi:
        with open(out_fn, 'w') as fo:
            T = read_int(fi)
            for i in range(1, T+1):
                case = read_case(fi)
                res = solver(case)
                write_case(fo, i, res)

################################################################################

def read_case(f):
    R1 = read_word(f).split(' ')
    return R1

def write_case(f, i, res):
    f.write('Case #%d: '%i)
    f.write('%s'%res)
    f.write('\n')

################################################################################

def solve_small(case):
    R1 = case
    audience, ss = R1
    if not R1:
        return 0
    else:
        ss = map(int, ss[:int(audience)+1])
        n_stands = 0
        n_friends = 0
        for r in ss:
            if r == 0:
                if n_stands > 0:
                    n_stands -= 1
                else:
                    n_friends += 1
            else:
                n_stands += r-1
        return n_friends

def solve_large(case):
    return solve_small(case)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("kind", type=int, help="small:1, large:2 select the kind of input")
    parser.add_argument("input_file", help="input file name")
    # parser.add_argument("output_file", help="output file name")
    args = parser.parse_args()
    solve(solve_small if args.kind == 1 else solve_large, args.input_file)
