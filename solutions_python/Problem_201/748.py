import sys


def debug(*args, sep=' ', end='\n'):
    print(*args, sep=sep, end=end, file=sys.stderr)


def ma_mi(n):
    n -= 1
    odd = n % 2
    n = n // 2
    return n + odd, n


def solve(n: int, k: int):
    debug(f'n={n}, k={k}')

    if k == 1:
        return ' '.join(map(str, ma_mi(n)))

    i = 0  # level
    t = 0
    while t < k:
        t += 2**i
        i += 1
    i -= 1

    t = k - (2**i - 1)  # number at level

    debug(f'level={i}, num={t}')

    # debug('experiment:', )

    road = list(map(int, format(t-1, f'0{i}b')[::-1]))
    debug(road)

    ma, mi = None, None

    for turn_left in road:
        ma, mi = ma_mi(n)
        debug(n, ma, mi)
        if turn_left:
            n = mi
        else:
            n = ma
        # print(n)

    return ' '.join(map(str, ma_mi(n)))


def save(i, result):
    print(f'Case #{i}: {result}')
    debug()


def main():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        result = solve(n, k)
        save(i+1, result)


if __name__ == '__main__':
    main()
