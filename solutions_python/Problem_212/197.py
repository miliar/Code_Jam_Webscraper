from collections import Counter, defaultdict

# 2 = 2, 1 * 2
# 3 = 3, 2 + 1, 1 * 3, 2 * 3
# 4 = 4, 3 + 1, 2 * 2, 2 + 1 * 2, 1 * 4, 2 * 4, 3 * 4
def solve(n, p, gs):
    result = 0
    g = defaultdict(int)
    for k, v in Counter([g % p for g in gs]).items():
        if k == 0:
            result += v
            continue
        g[k] = v
    # print(g)
    # result += g[0]
    if p == 2:
        # 1 * 2
        result += g[1] // 2
        g[1] %= 2

        # rest
        result += g[1] % 2
        return result
    elif p == 3:
        # 2 + 1
        m = min(g[2], g[1])
        result += m
        g[2] -= m
        g[1] -= m

        # 2 * 3
        result += g[2] // 3
        g[2] %= 3

        # 1 * 3
        result += g[1] // 3
        g[1] %= 3

        # rest
        if g[1] > 0 or g[2] > 0:
            result += 1
        return result
    elif p == 4:
        # 3 + 1
        m = min(g[3], g[1])
        result += m
        g[3] -= m
        g[1] -= m

        # 2 * 2
        result += g[2] // 2
        g[2] %= 2

        # 2 + 1 * 2
        m = min(g[2], g[1] // 2)
        result += m
        g[2] -= m
        g[1] -= m * 2

        # 3 * 2 + 2
        m = min(g[3] // 2, g[2])
        result += m
        g[3] -= m * 2
        g[2] -= m

        # 3 * 4
        result += g[3] // 4
        g[3] %= 4

        # 2 * 4
        result += g[2] // 4
        g[2] %= 4

        # 1 * 4
        result += g[1] // 4
        g[1] %= 4

        # rest
        if g[1] > 0 or g[2] > 0 or g[3] > 0:
            result += 1
        return result

def main():
    t = int(input())
    for i in range(t):
        n, p = map(int, input().split())
        gs = map(int, input().split())
        result = solve(n, p, gs)
        print("Case #{}: {}".format(i + 1, result))

if __name__ == '__main__':
    main()
