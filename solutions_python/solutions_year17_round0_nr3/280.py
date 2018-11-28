import sys

file_name = "C-large-practice"
sys.stdin = open(file_name + ".in", "r")
sys.stdout = open(file_name + ".out", "w")
input_line = sys.stdin.readline


def solve(n, k):
    if k == 1:
        ls = (n-1)//2
        rs = n//2
        return "{0} {1}".format(rs, ls)
    else:
        if k % 2 == 0:
            return solve(n//2, k//2)
        else:
            return solve((n-1)//2, k//2)

for case in range(1, int(input_line())+1):
    N, K = map(int, input_line().split())

    result = solve(N, K)
    print("Case #{0}: {1}".format(case, result))
