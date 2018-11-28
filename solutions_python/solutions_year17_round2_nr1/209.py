
for t in range(int(input())):
    D, N = map(int, input().split())
    H = [tuple(map(int, input().split())) for i in range(N)]

    last_t = max((D-Ki)/Si for Ki, Si in H)
    ans = D/last_t
    print('Case #{}: {}'.format(t+1, ans))