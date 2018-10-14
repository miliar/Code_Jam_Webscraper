T = int(input())

def ops(s):
    if s == '-':
        return '+'
    elif s == '+':
        return '-'

for t in range(T):
    signs, d = tuple(input().split())
    
    d = int(d)
    signs = list(signs)
    
    i = 0
    cnt = 0
    while i <= len(signs) - d:
        if signs[i] == '-':
            cnt += 1
            j = 0
            while j < d:
                signs[i + j] = ops(signs[i + j])
                j += 1
        i += 1
    good = True
    for s in signs:
        if s == '-':
            good = False
            break
    if good:
        print("Case #{}: {}".format(t + 1, cnt))
    else:
        print("Case #{}: IMPOSSIBLE".format(t + 1))