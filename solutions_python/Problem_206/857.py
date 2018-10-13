import sys


def solve(D, horses, test_case):
    
    max_time = max((D - offs) / speed for offs, speed in horses)
    speed = D / max_time
    print('Case #{}: {}'.format(test_case, speed))


def solve_all(fn):
    
    with open(fn) as f:
        T = int(f.readline().strip())
        for tc in range(1, T+1):
            D, N = [float(x) for x in f.readline().strip().split()]
            horses = []
            for n in range(int(N)):
                horses.append(tuple(float(x) for x in f.readline().strip().split()))
            solve(D, horses, tc)


if __name__ == '__main__':
    solve_all(sys.argv[1])