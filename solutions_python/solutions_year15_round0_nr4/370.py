ans = ['GABRIEL', 'RICHARD']

def solve(x, r, c):
    if (r * c) % x:
        return 1
    if x <= 2:
        return 0

    if r > c:
        r, c = c, r

    if x == 3:
        return r == 1

    if x == 4:
        return r <= 2    


for test in range(int(input())):
    x, r, c = map(int, input().split())

    print('Case #%d: %s' % (test + 1, ans[solve(x, r, c)]))
