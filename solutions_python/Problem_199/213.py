import sys

def get_min_flip(pancakes, size):
    """Get the minimal number of flips needed."""

    n_pancakes = len(pancakes)
    n_flips = 0

    for idx in range(n_pancakes):
        if pancakes[idx]:
            continue

        if idx + size - 1 >= n_pancakes:
            return None

        for i in range(size):
            pancakes[idx + i] = not pancakes[idx + i]
        n_flips += 1

        continue

    return n_flips


def main():
    """The main driver."""

    fp = open(sys.argv[1], 'r')
    for i, v in enumerate(fp):
        if i == 0:
            continue
        pancakes, size = v.split()
        res = get_min_flip(
            [i == '+' for i in pancakes], int(size)
        )
        if res is None:
            res = 'IMPOSSIBLE'
        print('Case #{}: {}'.format(i, res))
        continue


if __name__ == '__main__':
    main()
