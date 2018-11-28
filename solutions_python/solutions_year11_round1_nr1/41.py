from fractions import Fraction

def solve(N,PD,PG):
    FD = Fraction(PD, 100)
    FG = Fraction(PG, 100)
    if FD > 1: return False
    if FG > 1: return False
    if FG == 1 and FD < 1: return False
    if FG == 0 and FD > 0: return False
    if FD.denominator > N: return False
    return True

if __name__ == '__main__':
    import sys
    it = iter(sys.stdin)
    next(it)
    for i, line in enumerate(it, 1):
        N,PD,PG = map(int, line.split())
        print 'Case #{}: {}'.format(i, 'Possible' if solve(N,PD,PG) else 'Broken')
