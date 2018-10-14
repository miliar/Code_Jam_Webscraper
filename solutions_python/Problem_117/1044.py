from numpy.matlib import zeros
import sys


def check_line_less(N, M, arr, sx, sy, dx, dy, x):
    i = sx
    j = sy
    while i < N and j < M:
        if arr[i, j] > x:
            return False
        i += dx
        j += dy
    return True


def is_valid_pattern(N, M, arr):
    max_rows = zeros((N, 1), dtype=int)
    max_cols = zeros((M, 1), dtype=int)

    for i in range(N):
        for j in range(M):
            x = arr[i, j]
            if x > max_rows[i]:
                max_rows[i] = x
            if x > max_cols[j]:
                max_cols[j] = x

    for i in range(N):
        for j in range(M):
            x = arr[i, j]
            if x < max_rows[i] and x < max_cols[j]:
                return False

    return True


if __name__ == "__main__":
    if len(sys.argv) == 1:
        f_in = open("in.txt", "rt")
        f_out = sys.stdout
    else:
        f_in = open(sys.argv[1], "rt")
        f_out = open("out.txt", "wt")

    case_num = int(f_in.readline())

    for c in range(case_num):
        N, M = [int(x) for x in f_in.readline().split()]
        arr = zeros((N, M,), dtype=int)
        for i in range(N):
            line = f_in.readline().split()
            for j in range(M):
                arr[i, j] = line[j]

        #print arr
        result = N == 1 or M == 1 or is_valid_pattern(N, M, arr)
        if result:
            text = "YES"
        else:
            text = "NO"

        f_out.write("Case #%d: %s\n" % (c + 1, text))
    f_in.close()
    f_out.close()
