import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

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

def read_arr(f, R, reader=read_ints, *args, **kwargs):
    res = []
    for i in range(R):
        res.append(reader(f, *args, **kwargs))
    return res

def solve(solver, fn, out_fn=None):
    in_fn = fn + '.in'
    if out_fn is None:
        out_fn = fn + '.out'
    with open(in_fn, 'r') as fi:
        with open(out_fn, 'w') as fo:
            T = read_int(fi)
            for i in range(T):
                case = read_case(fi)
                res = solver(case)
                write_case(fo, i, res)

################################################################################

def read_case(f):
    X, R, C = read_ints(f)
    if R > C: return X, C, R
    return X, R, C

def write_case(f, i, res):
    f.write('Case #%d: '%(i+1))
    f.write('%s'%res)
    f.write('\n')


################################################################################

def solve_small(case):
    X, R, C = case
    if R*C % X != 0: return "RICHARD"
    if X <= 1: return "GABRIEL"
    if X == 2: return "GABRIEL"
    if X == 3:
        if R == 1: return "RICHARD"
        return "GABRIEL"
    if X == 4:
        if R == 1: return "RICHARD"
        if R == 2: return "RICHARD"
        if R == 3: return "GABRIEL"
        if R == 4: return "GABRIEL"
    
solve_large = solve_small

solve(solve_large, 'D-small-attempt0')
