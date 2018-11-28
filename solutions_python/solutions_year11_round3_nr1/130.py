#!/usr/bin/env python

from multiprocessing import Pool, cpu_count

def solve(table):
    R = len(table)
    C = len(table[0])

    for r in range(R-1):
        for c in range(C-1):
            if table[r][c] == '#':
                table[r][c] = '/'
                if table[r+1][c] == '#':
                    table[r+1][c] = '\\'
                else:
                    return ['Impossible']
                if table[r][c+1] == '#':
                    table[r][c+1] = '\\'
                else:
                    return ['Impossible']
                if table[r+1][c+1] == '#':
                    table[r+1][c+1] = '/'
                else:
                    return ['Impossible']

    for r in range(R):
        table[r] = str.join('', table[r])
        if '#' in table[r]:
            return ['Impossible']

    return table

if __name__ == '__main__':
    T = int(raw_input())

    testcases = []
    for t in range(T):
        R, C = [int(x) for x in raw_input().split()]

        table = []
        for c in range(R):
            table.append(list(raw_input().strip()))
            assert len(table[-1]) == C
        testcases.append(table)

    pool = Pool(cpu_count())
    results = pool.map(solve, testcases)
    #results = [solve(t) for t in testcases]

    for t in range(T):
        print 'Case #{0}:'.format(t+1)
        for line in results[t]:
            print line

