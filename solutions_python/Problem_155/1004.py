def read(f):
    N, p = f.readline().split()
    qs = [int(d) for d in p]
    return qs

def calc(data):
    standing = 0
    invitees = 0
    for i, n in enumerate(data):
        while i > standing:
            invitees += 1
            standing += 1
        standing += n
    return invitees

def write(solution):
    return str(solution)

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
