def solve(N):
    ds = [int(c) for c in str(N)]
    for i in range(1, len(ds)):
        if ds[i - 1] > ds[i]:
            ds[i - 1] -= 1
            ds[i:len(ds)] = [9] * (len(ds) - i)
            while ds[0] == 0:
                ds = ds[1:]
            return solve(int(''.join(map(str, ds))))
    return int(''.join(map(str, ds)))


T = int(input())
for tc in range(T):
    N = int(input())
    print('Case #{}: {}'.format(tc + 1, solve(N)))
