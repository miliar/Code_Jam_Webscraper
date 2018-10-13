import bisect

def get_stall(n):
    if n % 2 == 0:
        return n // 2, (n // 2) - 1
    else:
        return n // 2, n // 2

def bathroom_stalls(N, K):
    level, count = 1, 1
    n1, n2, k1, k2 = N - 1, N, 0, 1
    while K > count:
        level *= 2
        count += level
        if n2 % 2 == 0:
            n2, n1 = (n2 // 2), (n2 // 2 - 1)
            k2, k1 = k2, k2 + k1 * 2
        else:
            n2, n1 = (n2 // 2), (n2 // 2 - 1)
            k2, k1 = k2 * 2 + k1, k1
    n = n2 if K - count + level <= k2 else n1
    a, b = get_stall(n)
    return "{} {}".format(max(a, b), min(a, b))

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N, K = map(int, input().split())
        print("Case #{}: {}".format(i + 1, bathroom_stalls(N, K)))

