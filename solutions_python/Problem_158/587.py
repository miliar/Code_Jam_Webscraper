def oo(x, r, c):
    if x >= 7 or r * c % x != 0 or min(r, c) < x - 1:
        return 'RICHARD'
    else:
        return 'GABRIEL'

for t in range(int(input())):
    x, r, c = map(int, input().split())
    print('Case #', t + 1, ': ', oo(x, r, c), sep='')
