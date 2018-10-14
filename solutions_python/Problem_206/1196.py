# LINES_PER_CASE = 1
import numpy as np

def solve(x):
    K, S, N, D = x
    # sort_idx = np.argsort(K)
    # K, S, = K[sort_idx], S[sort_idx]
    t = np.max((D - K) / S)
    v = D / t
    return v


def read_case():
    D, N = map(int, input().split())
    LINES_PER_CASE = N
    lines = [input() for _ in range(LINES_PER_CASE)]
    KS = [list(map(int, s.split(' '))) for s in lines]
    K, S = np.array([KS]).T
    return K, S, N, D

# BEGIN CONSTANT PART

def print_result(i, *result):
    template = "Case #{}:" + " {}" * len(result)
    print(template.format(i, *result))


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        print_result(i+1, solve(read_case()))
