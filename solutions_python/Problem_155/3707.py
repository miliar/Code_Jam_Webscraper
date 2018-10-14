# skelethon copied from royf codejam 2014
import math
import itertools
# import numpy as NP

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
    if out_fn is None:
        out_fn = fn + '.out'
    with open(in_fn, 'r') as fi:
        with open(out_fn, 'w') as fo:
            T = read_int(fi)
            for i in range(T):
                case = read_case(fi)
                res = solver(case)
                write_case(fo, i + 1, res)

################################################################################

def read_case(f):
    tmp, Aud = read_words(f)
    shyMax = int(tmp)
    return [shyMax, Aud]

def write_case(f, i, res):
    f.write('Case #%d: '%i)
    f.write('%s'%res)
    f.write('\n')

################################################################################

def solve_small(case):
    res = 0
    shyMax, Aud = case
    reqStanding = len(Aud) - 1
    AudLessShy = Aud[0:-1]
    if reqStanding <= 0: return res
    while standingCount(AudLessShy) < reqStanding:

        AudLessShy = addAud(AudLessShy)
        res += 1
    return res

def solve_large(case):
    return solve_small(case)

def addAud(Aud, n=1):

    lstAud = [int(x) for x in list(Aud)]
    for j in range(n):
        i = 0
        while lstAud[i] == 9:
            if i + 1 < len(lstAud):

                i += 1
            else:

                return "".join([str(x) for x in lstAud]) 
        lstAud[i] += 1
    return "".join([str(x) for x in lstAud])

def standingCount(Aud):

    if len(Aud) == 1:

        return int(Aud)
    else:

        n = standingCount(Aud[0:-1])
        if n >= len(Aud) - 1 :

            return n + int(Aud[-1])
        else:

            return n 

