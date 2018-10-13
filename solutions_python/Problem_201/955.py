

def sp(n):
    if n == 0:
        return 0, 0
    if n % 2 == 0:
        return n // 2, n // 2
    else:
        return (n + 1) // 2, n // 2


def solve(N, K):

    l, r = sp(N - 1)
    while K // 2 > 0:
        N = l if K%2 == 0 else r
        N -= 1
        l, r = sp(N)
        K //= 2
    return '{} {}'.format(l, r)



if __name__ == '__main__':
    import fileinput
    f = fileinput.input()
    T = int(f.readline())
    for i in range(1, T + 1):
        N, K = map(int, f.readline().split())
        print("Case #{}: {}".format(i, solve(N, K)))

