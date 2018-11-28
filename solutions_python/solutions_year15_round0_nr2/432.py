tests = int(input())
for t in range(tests):
    d = int(input())
    a = list(map(int, input().split()))
    ans = max(a)
    for remain in range(1, max(a) + 1):
        here = sum((x - 1) // remain for x in a)
        ans = min(ans, here + remain)
    print('Case #{}: {}'.format(t + 1, ans))
