#!/usr/bin/python3

from sys import argv

def print_lawn(n, m, lawn):
    print('n={} m={}'.format(n, m))
    for i in range(n):
        print(' '.join(map(str, lawn[i])))
    print()

def possible(n, m, lawn):
    for i in range(n):
        for j in range(m):
            max_row, max_col = 0, 0
            for k in range(n):
                if max_col < lawn[k][j]: max_col = lawn[k][j]
            for k in range(m):
                if max_row < lawn[i][k]: max_row = lawn[i][k]
            if max_row > lawn[i][j] and max_col > lawn[i][j]:
                return False
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # Google Code Jam I/O
    infile = open(argv[1])
    cases = int(infile.readline())
    for i in range(cases):
        n, m = map(int, infile.readline().split())
        lawn = []
        for j in range(n):
            lawn.append(list(map(int, infile.readline().split())))
        print('Case #{}: {}'.format(i+1, "YES" if possible(n, m, lawn) else "NO"))
