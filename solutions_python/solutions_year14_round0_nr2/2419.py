

INPUT = 'B-large.in'
OUTPUT = 'B-large.out'


def solve(C, F, X):

    cps = 2.0
    farm_time = 0.0
    time = X / cps
    
    while True:
        farm_time += C / cps
        cps += F
        ntime = farm_time + X / cps
        if ntime < time:
            time = ntime
        else:
            break
    return time


if __name__ == '__main__':
    inp = open(INPUT)
    out = open(OUTPUT, 'w')
    
    T = int(inp.readline())

    for case in range(T):
        sol = solve(*map(float, inp.readline().split()))
        out.write('Case #%i: %.7f\n' % (case + 1, sol))