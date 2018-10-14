def is_tidy(N):
    return all(l <= r for l, r in zip(N, N[1:]))


def sweep(N):
    for i in range(len(N)-1):
        l, r = N[i], N[i+1]
        if l > r:
            N[i] = str(int(l)-1)
            for j in range(i+1, len(N)):
                N[j] = '9'
            return


def solve(N):
    while not is_tidy(N):
        sweep(N)
    return ''.join(N[N[0]=='0':])


for case in range(int(input())):
    ans = solve(list(input()))
    print('Case #%d: %s' % (case+1, ans))
