def is_tidy(n):
    last_c = '0'
    for c in str(n):
        if c < last_c:
            return False
        last_c = c
    return True

def solve(T, N):
    for i in range(N, 0, -1):
        if is_tidy(i):
            print("Case #{}: {}".format(T, i))
            return


if __name__ == '__main__':
    T = int(input())
    for i in range(1, T + 1):
        line = input().split()
        N = int(line[0])
        solve(i, N)
