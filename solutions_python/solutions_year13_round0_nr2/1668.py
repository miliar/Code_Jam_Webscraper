import sys
from itertools import product

def solve(matrix):
    n, m = len(matrix), len(matrix[0])
    max_hor, max_ver = [], []
    for i in xrange(n):
        max_hor.append(max(matrix[i]))
    for i in xrange(m):
        max_ver.append(max(matrix[k][i] for k in xrange(n)))

    for i, j in product(xrange(n), xrange(m)):
        if matrix[i][j] < max_hor[i] and matrix[i][j] < max_ver[j]:
            break
    else:
        return True

    return False

if __name__ == "__main__":
    n_cases = int(sys.stdin.readline().strip())
    for c in xrange(n_cases):
        matrix = []
        n, m = map(int, sys.stdin.readline().strip().split())
        for i in xrange(n):
            matrix.append(map(int, sys.stdin.readline().strip().split()))
        print "Case #{}: {}".format(c+1, "YES" if solve(matrix) else "NO")
