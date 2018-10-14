import sys

def lineitems():
    return sys.stdin.readline().strip().split(' ')

def main():
    numCases = int(sys.stdin.readline().strip())
    for caseNum in range(1, numCases + 1):
        print("Case #%d:" % caseNum, end=' ')
        [n, m] = map(int, lineitems())
        rows = set(range(n))
        cols = set(range(n))
        sumDiags = set(range(2 * n - 1))
        diffDiags = set(range(1-n, n))
        startingCells = set()
        startScore = 0
        for modelnum in range(m):
            [t, rstr, cstr] = lineitems()
            r, c = int(rstr) - 1, int(cstr) - 1
            if t == 'x' or t == 'o':
                rows.remove(r)
                cols.remove(c)
                startScore += 1
            if t == '+' or t == 'o':
                sumDiags.remove(r + c)
                diffDiags.remove(r - c)
                startScore += 1
            startingCells.add((r, c))
        rookCells = list(zip(rows, cols))
        bishopCells = []
        dsort = sorted(diffDiags, key=lambda s: -abs(s))
        for s in sumDiags:
            for (j, d) in enumerate(dsort):
                if s + d >= 0 and s + d < 2 * n and s - d >= 0 and s - d < 2 * n and (s + d) % 2 == 0:
                    r = (s + d) // 2
                    c = (s - d) // 2
                    bishopCells.append((r, c))
                    del dsort[j]
                    break
        rSet = set(rookCells)
        bSet = set(bishopCells)
        newQueens = rSet.intersection(bSet).union(rSet.intersection(startingCells)).union(bSet.intersection(startingCells))
        newRooks = rSet.difference(newQueens)
        newBishops = bSet.difference(newQueens)
        print(len(rSet) + len(bSet) + startScore, len(newQueens) + len(newRooks) + len(newBishops))
        for (r, c) in newQueens:
            print('o', r + 1, c + 1)
        for (r, c) in newRooks:
            print('x', r + 1, c + 1)
        for (r, c) in newBishops:
            print('+', r + 1, c + 1)

if __name__ == '__main__':
    main()
