import numpy as np


LINES_PER_CASE = 1


def solve(n):
    for i in range(len(n)-1, 0, -1):
        if n[i-1] > n[i]:
            n[i-1] -= 1
            n[i:] = 9
    m = int(''.join(map(str, n.tolist())))
    return m


def read_case():
    n = np.array([int(c) for c in input()], dtype=int)
    return n
    # lines = [input() for _ in range(LINES_PER_CASE)]
    # b, c = [int(s) for s in lines[0].split(' ')]
    # return b, c

# BEGIN CONSTANT PART

def print_result(i, *result):
    template = "Case #{}:" + " {}" * len(result)
    print(template.format(i, *result))


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        print_result(i+1, solve(read_case()))
