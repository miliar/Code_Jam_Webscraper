import io
import sys


def solve(f, F, C, X):
    f=0
    t=0
    while True:
        if time(X - C, f, F) <= time(X, f + 1, F):
            return t+time(X, f, F)
        else:
            t += C / (2 + f * F)
            f += 1


def farm(f, F, C, X):
    return C / (2 + f * F) + solve(f + 1, F, C, X)


def time(r, f, F):
    return r / (2 + f * F)


sample = u'''4
30.0 1.0 2.0
30.0 2.0 100.0
30.50000 3.14159 1999.19990
500.0 4.0 2000.0'''

# in_f = io.StringIO(sample)
in_f = open('B-large.in')
out_f = open('b-large.out','w')

T = int(in_f.readline())

sys.setrecursionlimit(10000)
for case in range(T):
    C, F, X = in_f.readline().split()
    out_f.write("Case #%s: %.7f\n" % (case + 1,
                                  solve( 0, float(F), float(C), float(X)) ))
