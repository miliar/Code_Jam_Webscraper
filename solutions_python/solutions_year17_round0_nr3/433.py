def get_sz(N, K):
    level = 0
    base = N
    while (1 << (level + 1)) - 1 < K:
        base = (base - 1) // 2
        level += 1

    n_inc_nodes = (N - ((1 << level) - 1)) - base * (1 << level)
    s = (1 << level)

    if K <= s + n_inc_nodes - 1:
        return base + 1
    else:
        return base

def main():
    TC = int(input())

    for tc in range(TC):
        N, K = map(int, input().split())
        sz = get_sz(N, K)
        if sz % 2 == 1:
            print('Case #{}: {} {}'.format(tc + 1, sz // 2, sz // 2))
        else:
            print('Case #{}: {} {}'.format(tc + 1, sz // 2, sz // 2 - 1))

if __name__ == '__main__':
    main()
