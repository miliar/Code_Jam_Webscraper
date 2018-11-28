import numpy as np


LINES_PER_CASE = 1


def solve(x):
    s, k = x
    n = len(s)
    y = 0
    for i in range(n - k + 1):
        if not s[i]:
            s[i:i+k] = ~s[i:i+k]
            y += 1
    if np.all(s):
        return y
    else:
        return 'IMPOSSIBLE'
    return 


def read_case():
    lines = [input() for _ in range(LINES_PER_CASE)]
    # a = int(input())
    s, k = lines[0].split(' ')
    s = np.array([c == '+' for c in s])
    k = int(k)
    return s, k

# BEGIN CONSTANT PART

def print_result(i, *result):
    template = "Case #{}:" + " {}" * len(result)
    print(template.format(i, *result))


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        print_result(i+1, solve(read_case()))
