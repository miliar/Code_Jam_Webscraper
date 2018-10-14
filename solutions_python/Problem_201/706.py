import sys


def get_buffer(n, k):
    large = n // 2
    small = n - 1 - large

    if k == 1:
        return max(large, small), min(large, small)
    else:
        if k % 2 == 1:
            return get_buffer(small, k // 2)
        else:
            return get_buffer(large, k // 2)


def read_input():
    num_rows = int(sys.stdin.readline())

    for i in range(1, num_rows + 1):
        line = sys.stdin.readline().strip().split(' ')
        n = int(line[0])
        k = int(line[-1])

        result = get_buffer(n, k)

        print('Case #{}: {} {}'.format(i, result[0], result[1]))


read_input()
