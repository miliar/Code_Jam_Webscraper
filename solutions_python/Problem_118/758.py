import sys
import numpy as np
import itertools as it
import gmpy2 as g2

def nums_line(f, dtype=int):
    return np.array([dtype(k) for k in f.readline().strip().split()])

def main(argv=None):
    if not argv:
        argv = sys.argv[1:]
    filename = argv[0] if argv else 'test.in'

    with open(filename) as f:
        num_cases = int(f.readline())
        for case_no in xrange(1, num_cases+1):
            a, b = nums_line(f, dtype=g2.mpz)
            count = count_fair(a, b)
            print "Case #{}: {}".format(case_no, count)

def count_fair(a, b, disp=False):
    count = 0
    a2, t = g2.isqrt_rem(a)
    if t != 0:
        a2 += 1
    b2, t = g2.isqrt_rem(b)
    for p in iter_p(a2, b2):
        if is_pali((p*p).digits()):
            if disp:
                print count+1, (p*p).num_digits(), p, p*p
            count += 1
    return count

def iter_p(a, b):
    a = g2.mpz(a)
    b = g2.mpz(b)

    ds = a.digits()
    
    is_even = (len(ds) % 2) == 0
    nd = (len(ds) + 1) / 2
    cutoff = 10 ** nd

    digits = ds[:nd]
    value = g2.mpz(digits)
    n = make_pali(digits, is_even)

    if n < a:
        value += 1
        digits = value.digits()
        n = make_pali(digits, is_even)
        if n < a:
            print >> sys.stderr, "ERROR: Out of bounds."

    while n <= b:
        yield n
        value += 1
        if value >= cutoff:
            if not is_even:
                value = g2.mpz(cutoff / 10)
                is_even = True
            else:
                nd += 1
                cutoff *= 10
                is_even = False
        digits = value.digits()
        n = make_pali(digits, is_even)

def make_pali(s, is_even):
    if is_even:
        middle = ""
    else:
        middle = s[-1]
        s = s[:-1]
    return g2.mpz(s + middle + s[::-1])

def is_pali(s):
    i = 0
    j = len(s) - 1
    while i * 2 < len(s) - 1:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

if __name__ == '__main__':
    if sys.argv[1] == "-d":
        count_fair(0, 10**50, True)
    else:
        main()
