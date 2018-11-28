from wrap import *
from fractions import gcd

def does_divide(a, b):
    return (1.0*a / b) == (a/b)

def check_possibility(n, pd, pg):
    if ((pg == 100) and (pd < 100)) or ((pg == 0) and (pd > 0)):
        return False
    min_coeff = 100/gcd(pd, 100)
    return min_coeff <= n

def answer(f):
    x = f.readline()
    n, pd, pg = make_ints(x)
    if check_possibility(n, pd, pg):
        return "Possible"
    else:
        return "Broken"

cjwrap(answer, 'A-large.in')