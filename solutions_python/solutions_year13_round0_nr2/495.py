def solve(lawn, n, m):
    for i in range(n):
        for j in range(m):
            v = lawn[i][j]
            passed = False
            for k in range(n):
                if v < lawn[k][j]:
                    for k in range(m):
                        if v < lawn[i][k]:
                            break
                    else:
                        passed = True
                    break
            else:
                passed = True
            if not passed:
                return 'NO'
    return 'YES'

n = input()

for i in range(n):
    [n, m] = [int(x) for x in raw_input().split()]

    l = []
    for j in range(n):
        l.append([int(x) for x in raw_input().split()])
    print('Case #{}: {}'.format(i + 1, solve(l, n, m)))
