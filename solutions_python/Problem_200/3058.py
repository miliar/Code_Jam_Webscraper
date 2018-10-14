import sys


def check_tidy(s: str) -> int:
    for idx in range(0, len(s) - 1):
        if s[idx] > s[idx + 1]:
            return idx
    return -1


def tidy(n: int) -> int:
    while True:
        s = str(n)
        untidy_idx = check_tidy(s)
        if untidy_idx == -1:
            return n
        else:
            n = n - int(''.join(s[untidy_idx + 1:])) - 1


def main():
    fni = sys.argv[1]

    with open(fni) as fi:
        fi.readline()
        for idx, line in enumerate(fi):
            n = int(line.strip())
            solution = tidy(n)

            print('Case #{}: {}'.format(idx + 1, solution))


if __name__ == '__main__':
    main()
