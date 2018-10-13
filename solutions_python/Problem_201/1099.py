from collections import Counter


def solve(n, k):
    d = Counter([n])
    for i in range(k):
        a = n // 2
        b = (n - 1) // 2
        if a == 0:
            break
        d[a] += 1
        d[b] += 1
        d[n] -= 1
        if d[n] == 0:
            del d[n]
            n = max(d)
    return a, b


def test_solve():
    assert solve(4, 2) == (1, 0)
    assert solve(5, 2) == (1, 0)
    assert solve(6, 2) == (1, 1)
    assert solve(1000, 1000) == (0, 0)
    assert solve(1000, 1) == (500, 499)


def main():
    T = int(input())
    for i in range(1, T + 1):
        N, K = map(int, input().split())
        print('Case #{}: {} {}'.format(i, *solve(N, K)))


if __name__ == '__main__':
    main()
