import sys

STDOUT = sys.stdout
STDIN = sys.stdin


def breakpt():
    def swap_bufs():
        global STDIN, STDOUT
        sys.stdin, STDIN = STDIN, sys.stdin
        sys.stdout, STDOUT = STDOUT, sys.stdout

    swap_bufs()
    import IPython
    IPython.embed()
    swap_bufs()


def tidy(s):
    for i in range(len(s) - 1):
        if not s[i] <= s[i + 1]:
            return False, i
    return True, None


def t_case():
    s = [*map(int, list(input()))]
    good = False
    while not good:
        good, i = tidy(s)
        if not good:
            s[i] -= 1
            for j in range(i + 1, len(s)):
                s[j] = 9

    for i in range(len(s)):
        if s[i] != 0:
            s = s[i:]
            break

    print(''.join(map(str, s)))


def main(*args):
    with open(args[1], 'r') as fin:
        with open(args[2], 'w') as fout:
            sys.stdout = fout
            sys.stdin = fin
            n = int(input())
            for i in range(n):
                print(f'Case #{i+1}: ', end='')
                t_case()


if __name__ == '__main__':
    main(*sys.argv)
