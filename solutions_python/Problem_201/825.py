import sys


def min_max_free(n, k):
    assert 1 <= k <= n
    n -= 1
    if k == 1:
        return n // 2 + n % 2, n // 2
    k -= 1
    if k % 2 == 0:
        return min_max_free(n // 2, k // 2)
    else:
        return min_max_free(n // 2 + n % 2, k // 2 + k % 2)


if __name__ == '__main__':
    filename = sys.argv[1]

    with open(filename) as f:
        next(f)  # skip header

        for i, line in enumerate(f):
            n, k = map(int, line.strip().split(' '))
            print('Case #{}: {}'.format(i + 1, ' '.join(map(str, min_max_free(n, k)))))
