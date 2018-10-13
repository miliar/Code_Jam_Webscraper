import math
import sys

PI = math.pi


def max_surface(P, K):
    # sort by reverse radius
    P.sort(key=lambda p : p[0], reverse=True)

    surface = [0] * len(P)
    for i in range(len(P)):
        # select K-1 best pancakes
        best = sorted(P[i+1:], key=lambda p : 2*p[0]*p[1], reverse=True)
        if len(best) < K-1:
            continue
        best = best[0:K-1]
        surface[i] = P[i][0]**2 + \
                     2*P[i][0]*P[i][1] + \
                     sum([2*p[0]*p[1] for p in best])
    return PI*max(surface)


if __name__ == '__main__':
    filename = sys.argv[1]

    with open(filename) as f:
        T = int(next(f))  # number of test cases
        for i in range(T):
            # N : number of pancakes
            # K : number of pancakes to select
            N, K = map(int, next(f).split(' '))
            P = []  # pancakes (radius, height)
            for j in range(N):
                R_i, H_i = map(int, next(f).split(' '))
                P.append((R_i, H_i))
            print('Case #{}: {:.15f}'.format(i + 1, max_surface(P, K)))
