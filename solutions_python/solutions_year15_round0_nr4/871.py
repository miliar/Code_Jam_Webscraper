def win(t, s):
    print('Case #{0}: {1}'.format(t + 1, s))
def gwin(t):
    win(t, 'GABRIEL')
def rwin(t):
    win(t, 'RICHARD')

T = int(input())
for t in range(T):
    X, R, C = map(int, input().split())
    if X > max(R, C):
        rwin(t)
    elif (X + 1) // 2  > min(R, C):
        rwin(t)
    elif X >= 7:
        rwin(t)
    elif R * C % X:
        rwin(t)
    elif X > 3 and R * C == X * 2:
        rwin(t)
    else:
        gwin(t)
