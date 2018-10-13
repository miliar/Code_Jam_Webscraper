import sys
assert sys.version_info >= (3, 5)


def solve(prefix):
    N, R, O, Y, G, B, V = [int(_) for _ in input().split()]
    assert O == G == V == 0
    assert R + Y + B == N
    cand = [(R, 'R'), (Y, 'Y'), (B, 'B')]
    cand.sort(reverse=True)
    ans = [None for _ in range(N)]
    n, c = cand[0]
    if n*2 > N:
        print('{}{}'.format(prefix, 'IMPOSSIBLE'))
        return
    ci = 0
    i = 0
    while ci < n:
        ans[i] = c
        ci += 1
        i += 2
    n, c = cand[1]
    ci = 0
    i = N-1
    while ci < n:
        if ans[i] is not None:
            i -= 1
        ans[i] = c
        ci += 1
        i -= 2
    n, c = cand[2]
    ans = ''.join(c if _ is None else _ for _ in ans)
    print('{}{}'.format(prefix, ans))


def main():
    T = int(input())
    for t in range(T):
        solve(prefix='Case #{}: '.format(t+1))


if __name__ == '__main__':
    main()
