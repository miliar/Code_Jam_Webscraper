from __future__ import division
import fileinput
from operator import itemgetter

#sorted(L, key=itemgetter(2))
def main():
    fin = fileinput.input()
    T = int(next(fin))  # number of test cases
    for case in range(1, T + 1):
        D, N = map(int, next(fin).split(' '))
        L = [[0, 0, 0] for i in range(N)]
        for i in range(N):
            L[i][0], L[i][1] = map(int, next(fin).split(' '))
            x = D - L[i][0]
            L[i][2] = x / L[i][1]

        L = sorted(L, key=itemgetter(2), reverse=True)
        t = L[0][2]

        print("Case #{}: {}".format(case, D / t))

if __name__ == '__main__':
    main()