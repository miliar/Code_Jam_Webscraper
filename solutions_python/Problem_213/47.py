import math
from multiprocessing import Pool

def solve(args):
    N, C, M, P, B = args
    count = [0] * C
    for i in range(M):
        count[B[i] - 1] += 1
    ans = max(count)
    ans1 = 0
    while True:
        # print ans, ans1
        ans1 = 0
        seats = [[] for _ in range(N)]
        for i in range(M):
            seats[P[i] - 1].append(B[i])
        left = 0
        for i in range(0, N):
            # print len(seats[i]) - ans
            if len(seats[i]) <= ans:
                left += ans - len(seats[i])
            elif left < len(seats[i]) - ans:
                ans += 1
                break
            else:
                left -= len(seats[i]) - ans
                ans1 += len(seats[i]) - ans
        else:
            break
    return '{} {}'.format(ans, ans1)

def formatter(arg):
    return 'Case #{0}: {1}'.format(arg[0] + 1, arg[1])

def input_gen(T):
    for i in xrange(1, T + 1):
        N, C, M = map(int, raw_input().strip().split())
        P = []
        B = []
        for j in range(M):
            p, b = map(int, raw_input().strip().split())
            P.append(p)
            B.append(b)
        yield N, C, M, P, B

def main():
    CORES = 1
    p = Pool(CORES)
    T = input()
    print '\n'.join(map(formatter, enumerate(
        # p.map(solve, input_gen(T), T / CORES)
        p.map(solve, input_gen(T), 1)
    )))
    # for arg in input_gen(T):
    #     print formatter((1, solve(arg)))

def main1():
    print(solve((3, 4, [1, 1, 1, 1, 1, 1, 1, 1, 1])))

if __name__ == '__main__':
    main()
    # main1()
