import sys

def solve():
    D, N = map(int, sys.stdin.readline().rstrip().split())

    max_time = 0
    for i in range(N):
        K, S = map(int, sys.stdin.readline().rstrip().split())
        time_taken = (D-K)*1.0/S
        if time_taken >= max_time:
            slow_K = K
            slow_S = S
            max_time = time_taken

    cruise_speed = D * slow_S * 1.0 / ( D - slow_K)
    return cruise_speed


def main():
    T = int(sys.stdin.readline().rstrip())
    for t in range(1, T+1):
        print 'Case #{}: {:.6f}'.format(t, solve())

if __name__ == "__main__":
    main()
