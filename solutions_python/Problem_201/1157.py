DEBUG = False


def printd(s):
    if DEBUG:
        print(s)


def solve(N, K):
    if N == K:
        return "{} {}".format(0, 0)

    c = get_split_pow(K)
    printd("c:{}".format(c))
    avg_l = int((N - (2 ** c - 1)) / (2 ** c))
    printd("avg_l:{}".format(avg_l))
    hcount = N - (2 ** c - 1) - 2 ** c * avg_l
    if K - (2 ** c - 1) - hcount > 0:
        avg = avg_l
    else:
        avg = avg_l + 1
    ls, rs = get_empty_stalls(avg)
    return "{} {}".format(max(ls, rs), min(ls, rs))


def get_empty_stalls(n):
    if n % 2 == 0:
        ls = n / 2 - 1
        rs = n / 2
    else:
        ls = (n - 1) / 2
        rs = (n - 1) / 2
    return int(ls), int(rs)


def get_split_pow(n):
    if n == 0:
        return 0
    pow = 0
    while True:
        if 2 ** pow > n:
            break
        else:
            pow += 1
    return pow - 1


def main():
    n = int(input())
    for i in range(1, n + 1):
        N, K = [int(s) for s in input().split(" ")]
        out = solve(N, K)
        print("Case #{}: {}".format(i, out))

if __name__ == "__main__":
    main()
