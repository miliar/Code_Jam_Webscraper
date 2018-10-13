def a(board):
    open_space = False
    d1 = {'X': 0, 'O': 0}
    d2 = {'X': 0, 'O': 0}
    
    c = [{'X': 0, 'O': 0} for i in range(4)]
    for j, row in enumerate(board):
        r = {'X': 0, 'O': 0}
        for i, p in enumerate(row):
            if p == '.':
                open_space = True
            elif p == 'T':
                if i == j:
                    d1['X'] += 1
                    d1['O'] += 1
                if i == 3-j:
                    d2['X'] += 1
                    d2['O'] += 1
                c[i]['X'] += 1
                c[i]['O'] += 1
                r['X'] += 1
                r['O'] += 1
            else:
                c[i][p] += 1
                r[p] += 1
                if i == j:
                    d1[p] += 1
                if i == 3-j:
                    d2[p] += 1
        if r['O'] > 3:
            return 'O won'
        elif r['X'] > 3:
            return 'X won'
    for col in c:
        if col['O'] > 3:
            return 'O won'
        elif col['X'] > 3:
            return 'X won'
                
    if d1['O'] > 3:
        return 'O won'
    elif d1['X'] > 3:
        return 'X won'
    
    if d2['O'] > 3:
        return 'O won'
    elif d2['X'] > 3:
        return 'X won'
    if open_space:
        return 'Game has not completed'
    return 'Draw'

if __name__ == "__main__":
    import sys
    cases = sys.stdin.readline()
    for tc in range(1, int(cases)+1):
        board = [sys.stdin.readline()[:-1],
                 sys.stdin.readline()[:-1],
                 sys.stdin.readline()[:-1],
                 sys.stdin.readline()[:-1]]
        print 'Case #{0}: {1}'.format(tc, a(board))
        sys.stdin.readline()
