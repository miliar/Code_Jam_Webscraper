
import numpy as np


def solve(N):
    N = np.array(map(int, str(N)))

    for i in range(len(N)-2, -1, -1):
        if N[i+1] < N[i]:
            N[i] -= 1
            N[i+1:] = 9
    for c in range(len(N)):
        if N[c] != 0:
            break

    return int("".join(map(str, N[c:])))


if __name__ == "__main__":
    T = int(raw_input())
    for t in range(1, T+1):
        N = int(raw_input())
        print "Case #%d: %d" % (t, solve(N))
