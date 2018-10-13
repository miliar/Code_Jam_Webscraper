from sys import stdin

T = int(stdin.readline().strip())
for i in range(T):
    X, R, C = [int(e) for e in stdin.readline().strip().split(' ')]
    if X == 1:
        res = 'GABRIEL'
    else:
        if R < (X-1) or C < (X-1) or R * C % X > 0:
            res = 'RICHARD'
        else:
            res = 'GABRIEL'
    print 'Case #{}: {}'.format(i+1, res)
