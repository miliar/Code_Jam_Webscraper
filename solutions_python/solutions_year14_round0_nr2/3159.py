INF = 1e99

def solve(C, F, X):
    rate = 2.0
    elapsed = 0.0
    best = INF

    while True:
        wait_time = X/rate
        if elapsed + wait_time < best:
            best = elapsed + wait_time

        buy_time = C/rate
        if wait_time < buy_time:
            return best

        next_wait_time = buy_time + X/(rate+F)
        if next_wait_time >= wait_time:
            return best

        elapsed += buy_time
        rate += F


def solve_one():
    C, F, X = map(float, raw_input().split())
    return str(solve(C, F, X))


def main():
    T = int(raw_input())

    for s in range(1,T+1):
        print ('Case #%d: ' % s) + solve_one()


if __name__ == '__main__':
    main()
