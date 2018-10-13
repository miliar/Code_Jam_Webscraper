tests = int(input())
for t in range(tests):
    s = input().split()[1]
    a = []
    for i, c in enumerate(s):
        a += [i] * int(c)
    ans = max(0, max(x - i for i, x in enumerate(a)))
    print('Case #{}: {}'.format(t+1, ans))

