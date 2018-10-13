import sys


def get_swap(pancakes, k):
    if '-' in pancakes[:len(pancakes) - k + 1]:
        return pancakes.index('-')
    else:
        return max(len(pancakes) - k - pancakes[::-1].index('-'), 0)


def invert(pancakes, start, k):
    for i in range(start, start + k):
        pancakes[i] = '+' if pancakes[i] == '-' else '-'


def answer(p, k):
    swaps = set()
    p = list(p)

    while '-' in p:
        swap = get_swap(p, k)

        if swap in swaps:
            return None

        invert(p, swap, k)

        swaps.add(swap)

    return len(swaps)


def read_input():
    num_rows = int(sys.stdin.readline())

    for i in range(1, num_rows + 1):
        line = sys.stdin.readline().split(' ')
        p = line[0]
        k = line[-1]

        result = answer(p, int(k))

        print('Case #{}: {}'.format(i, result if result is not None else 'IMPOSSIBLE'))


read_input()
