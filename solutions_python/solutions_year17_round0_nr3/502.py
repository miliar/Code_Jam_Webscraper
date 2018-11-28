cache = {}

def f4(n):
    if n < 2:
        return {0: 1}
    if n == 2:
        return {1: 1, 0: 1}
    if n in cache:
        return cache[n]
    z = n - 1
    ans = {z: 1}
    for x, y in f4(z // 2).items():
        if x not in ans:
            ans[x] = y
        else:
            ans[x] += y
    for x, y in f4(z - z // 2).items():
        if x not in ans:
            ans[x] = y
        else:
            ans[x] += y
    cache[n] = ans
    return ans


def F(n, k):
    z = sorted(f4(n).items(), reverse=True)
    for x, y in z:
        if k < y:
            return x
        k -= y
    return 0


def main2():
    n, k = [int(x) for x in input().split()]
    ans = F(n, k - 1)
    print(ans - ans // 2, ans // 2)


def main():
    n = int(input())
    for i in range(1, n + 1):
        print('Case #{}: '.format(i), end='')
        main2()

if __name__ == "__main__":
    main()
