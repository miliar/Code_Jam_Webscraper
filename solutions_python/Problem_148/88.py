import math
import sys
import operator
sys.setrecursionlimit(10000) # 10000 is an example, try with different values

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
    
def read_floats(f, d=' '):
    return [float(x) for x in read_words(f, d)]

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
    N, X= read_ints(f)
    Ss = read_ints(f)
    return N, X, Ss

def write_case(f, i, res):
    f.write('Case #%d: '%(i+1))
    f.write('%d\n'%res)


################################################################################
def solve_small(case):
    N, X, Ss = case
    table = [0] * 701
    for i in range(N):
        table[Ss[i]] += 1
    Ss.sort()
    
    res = 0
    nleft = N
    for i in range(N):
        if nleft == 0: break
        t = Ss[i]
        if table[Ss[i]] == 0:
            continue
        table[t] -= 1
        
        s = X - t
        
        j = s
        while j > 0:
            if table[j] > 0:
                table[j] -= 1
                nleft -= 1
                break
            j -= 1
        nleft -= 1
        res += 1
    return res
    
solve_large = solve_small

solve(solve_large, 'A')

