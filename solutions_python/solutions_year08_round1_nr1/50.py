def solve(x, y):
    res = 0
    xx, yy = sorted(x), sorted(y)
    for i in range(len(xx)): res += xx[-i-1] * yy[i]
    return res

for n in range(input()):
    input()
    x = map(int, raw_input().split())
    y = map(int, raw_input().split())
    print("Case #%d: %d" %(n + 1, solve(x, y)))