import sys
from heapq import heappop
from heapq import heappush

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


# def main(*args):
#     with open(args[1], 'r') as fin:
#         with open(args[2], 'w') as fout:
#             sys.stdout = fout
#             sys.stdin = fin
#             n = int(1e18)
#             for k in range(0, 100):
#                 ans = solve(n, k + 1)
#                 print(f'Case #{k+1}: {ans}')


def main(*args):
    with open(args[1], 'r') as fin:
        with open(args[2], 'w') as fout:
            sys.stdout = fout
            sys.stdin = fin
            n = int(input())
            for i in range(n):
                ans = t_case()
                print(f'Case #{i+1}: {ans}')


def t_case():
    n, k = map(int, input().split())
    return solve(n, k)


def solve(n, k):
    h = [-n]
    for i in range(k):
        x = -heappop(h)
        x -= 1
        l = x // 2
        r = x - l
        heappush(h, -l)
        heappush(h, -r)
        if i == k - 1:
            assert r >= l
            return f'{r} {l}'


if __name__ == '__main__':
    main(*sys.argv)
