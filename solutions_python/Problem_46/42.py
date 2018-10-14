#!/usr/bin/env python3

from sys import stdin, stdout, stderr

def solve_case(case):
    #print(case, file=stderr)
    N, matrix = case
    for i in range(N):
        try:
            last = list(reversed(matrix[i])).index(1)
        except ValueError:
            last = N
        matrix[i] = N - 1 - last
    #print(matrix)
    count = 0
    for k in range(1, N + 1):
        i = 0
        while i < k:
            if matrix[i] == N - k + i + 1:
                j = i
                while matrix[j] >= N - k + i + 1:
                    j += 1
                matrix[i: j + 1] = [matrix[j]] + matrix[i: j]
                count += j - i
                i = j
            i += 1
        #print(*matrix, sep='\n')
        #print()
    return count

def read_case():
    N = int(input())
    matrix = [list(map(int, list(input()))) for i in range(N)]
    return N, matrix

def print_case(i, ans):
    s = "Case #%d: %s" % (i, ans)
    print(s)

def main():
    for i in range(1, int(input()) + 1):
        print_case(i, solve_case(read_case()))

if __name__ == "__main__":
    main()

