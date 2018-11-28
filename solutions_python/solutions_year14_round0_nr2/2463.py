import itertools
T = int(input())

for test in range(T):
    c, f, x = map(float, input().split())

    accs = []
    for i in range(0, 200001):
        accs.append(c / (2+f*i))
    accs = list(itertools.accumulate(accs))

    minn = float('inf')
    for k in range(0, 200001):
        ans = 0 if k==0 else accs[k-1]
        ans += x / (2 + k*f)
        minn = min(minn, ans)
    print('Case #{}: {}'.format(test+1, minn))
