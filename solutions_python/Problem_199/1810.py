import sys
read = lambda f=int: map(f, sys.stdin.readline().split())
T, = read()
for case in range(T):
    x, k = sys.stdin.readline().split()
    k = int(k)
    x = [1 if xi == '+' else 0 for xi in x]
    res = 0
    for i in range(len(x)-k+1):
        if x[i] == 0:
            res += 1
            for j in range(i, i+k):
                x[j] = 1-x[j]
    #print(x)
    if all(x):
        print('Case #{}: {}'.format(case+1, res))
    else:
        print('Case #{}: IMPOSSIBLE'.format(case+1))

