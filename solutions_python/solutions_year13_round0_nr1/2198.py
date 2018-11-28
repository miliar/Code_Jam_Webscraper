SQUARE_SZ = 4

def read_case():
    sq = [ [] for i in range(SQUARE_SZ) ]
    for r in range(SQUARE_SZ):
        st = ''
        while len(st) < SQUARE_SZ: st = input()
        sq[r] = st[0:SQUARE_SZ]
    return sq

def solve_case(sq):
    scored = { 'X': False, 'O': False }
    for plr in ['X','O']:
        for r in range(SQUARE_SZ):
            full = True
            for s in range(SQUARE_SZ):
                full = full and sq[r][s] in [plr, 'T']
            if full:
                scored[plr] = True
        for c in range(SQUARE_SZ):
            full = True
            for r in range(SQUARE_SZ):
                full = full and sq[r][c] in [plr, 'T']
            if full:
                scored[plr] = True
        dfull_tl = True; dfull_tr = True
        for d1 in range(SQUARE_SZ):
            dfull_tl = dfull_tl and sq[d1][d1] in [plr, 'T']
            dfull_tr = dfull_tr and sq[d1][SQUARE_SZ-d1-1] in [plr, 'T']
        if dfull_tl:
            scored[plr] = True
        if dfull_tr:
            scored[plr] = True

    if scored['X'] and not scored['O']: return 'X won'
    if scored['O'] and not scored['X']: return 'O won'
    else: return 'Game has not completed' if True in [ ('.' in r) for r in sq ] else 'Draw'


if __name__ == '__main__':
    T = int(input())
    for t in range(1, T+1):
        res = solve_case(read_case())
        print("Case #{}: {}".format(t, res))
