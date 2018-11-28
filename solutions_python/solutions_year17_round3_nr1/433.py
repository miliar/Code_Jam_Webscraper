import math


def read_ints():
    return [int(x) for x in input().split(' ')]


def area(Rs, Hs):
    return math.pi * Rs[0] ** 2 + sum(2*math.pi*R*H for (R, H) in zip(Rs, Hs))



def solve(Rs, Hs, K):
    N = len(Rs)

    max_area = 0
    for bottom in range(N):
        choices = sorted(
            list(range(0, bottom)) + list(range(bottom+1, N)),
            key=lambda i: -Rs[i]*Hs[i]
        )
        max_area = max(max_area,
                       area([Rs[bottom]] + [Rs[i] for i in choices[:K-1]],
                            [Hs[bottom]] + [Hs[i] for i in choices[:K - 1]]))
    return max_area







def main():
    T = int(input())
    for i in range(T):
        Rs, Hs = [], []
        N, K = read_ints()
        for j in range(N):
            R, H = read_ints()
            Rs.append(R)
            Hs.append(H)

        solution = solve(Rs, Hs, K)
        print('Case #{}: {}'.format(i+1, solution))


if __name__ == '__main__':
    main()