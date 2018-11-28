
MT = 'GABRIEL'
MF = 'RICHARD'

def solve():
    x, n, m = map(int, input().split())
    if x == 1 and n * m == 1:
        print(MT)
        return
    if x == 2 and n * m == 2:
        print(MT)
        return
    if n * m <= x or (n * m) % x != 0:
        print(MF)
        return
    if x == 4 and max(n, m) == 4 and min(n, m) == 2:
        print(MF)
        return
    print(MT)




t = int(input())
for tests in range(t):
    print('Case #', tests + 1, ': ', sep='', end='')
    solve()
