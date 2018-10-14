def f(d, houses):
    t = max((d - house[0])/house[1] for house in houses)
    return d/t

t = int(input())
for testCase in range(t):
    d, n = map(int, input().split())
    houses = []

    for i in range(n):
        p, s = map(int, input().split())
        houses.append((p,s))

    print('Case #' + str(testCase+1) + ':', '{0:.6f}'.format(f(d, houses)))
