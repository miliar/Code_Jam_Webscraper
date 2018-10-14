def solve(i, N):
    ns = [int(n) for n in str(N)]
    def iter(j, n):
        if j == len(ns):
            return []
        else:
            aj = ns[j]
            if aj >= n:
                ns_ = iter(j + 1, aj)
                if ns_ != None:
                    return [aj] + ns_
                elif aj > n:
                    return [aj - 1] + [9] * (len(ns) - j - 1)
                else:
                    return None
    ans = iter(0, 0)
    ans = int(''.join([str(n) for n in ans]))
    print('Case #{}: {}'.format(i, ans))

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        solve(i + 1, N)

