def read(f):
    X, R, C = [int(n) for n in f.readline().split()]
    return X, R, C

def calc(data):
    X, R, C = data
    small_results = {
        2: {(1, 1): 'R',
            (1, 2): 'G',
            (1, 3): 'R',
            (1, 4): 'G',
            (2, 2): 'G',
            (2, 3): 'G',
            (2, 4): 'G',
            (3, 3): 'R',
            (3, 4): 'G',
            (4, 4): 'G'},
        3: {(1, 1): 'R',
            (1, 2): 'R',
            (1, 3): 'R',
            (1, 4): 'R',
            (2, 2): 'R',
            (2, 3): 'G',
            (2, 4): 'R',
            (3, 3): 'G',
            (3, 4): 'G',
            (4, 4): 'R'},
        4: {(1, 1): 'R',
            (1, 2): 'R',
            (1, 3): 'R',
            (1, 4): 'R',
            (2, 2): 'R',
            (2, 3): 'R',
            (2, 4): 'R',
            (3, 3): 'R',
            (3, 4): 'G',
            (4, 4): 'G'}
    }
    if X == 1:
        return 'G'
    if R > C:
        R, C = C, R
    return small_results[X][(R, C)]

def write(solution):
    if solution == 'G':
        return 'GABRIEL'
    else:
        return 'RICHARD'

def solve(f):
    data = read(f)
    solution = calc(data)
    return write(solution)

if __name__ == '__main__':
    import sys
    with open(sys.argv[1]) as f:
        T = int(f.readline())
        for t in range(1, T+1):
            print('Case #{t}: {solution}'.format(t=t, solution=solve(f)))
