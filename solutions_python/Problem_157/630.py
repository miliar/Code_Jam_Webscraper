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
    L, X = read_ints(f)
    ss = read_word(f)
    seq = []
    for s in ss:
        if s == 'i': seq.append(2)
        if s == 'j': seq.append(3)
        if s == 'k': seq.append(4)
    return L, X, seq

def write_case(f, i, res):
    f.write('Case #%d: '%(i+1))
    f.write('%s'%res)
    f.write('\n')


################################################################################
quatmap = [[0,0,0,0,0], [0, 1, 2, 3, 4], [0, 2, -1, 4, -3], [0, 3, -4, -1, 2],[0, 4, 3, -2, -1]]

def quat(a, b):
    sgn = -1
    if a*b > 0: sgn = 1
    return sgn * quatmap[abs(a)][abs(b)]

def red(ss):
    res = 1
    for s in ss:
        res = quat(res, s)
    return res

def solve_small(case):
    print case
    L, X, s = case
    if L * X < 3: return "NO"
    if len(s) == 1: return "NO"
    s = s * X
    res = red(s)
    if res != -1: return "NO"
    for i in range(1, len(s)-1):
        # print 'i', s[:i]
        si = red(s[:i])
        if si != 2: continue
        for j in range(i+1, len(s)):
            # print 'j', s[i:j]
            sj = red(s[i:j])
            if sj != 3: continue
            # print 'k', s[j:]
            sk = red(s[j:])
            if sk == 4: return "YES"
    return "NO"
    
def solve_large(case):
    L, X, s = case
    if L * X < 3: return "NO"
    if len(s) <= 2: return "NO"
    s = s * X
    res = red(s)
    if res == -1: return "YES"
    return "NO"

solve(solve_small, 'C-small-attempt2')
