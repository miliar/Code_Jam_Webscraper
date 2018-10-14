T = int(input())
for t in range(0, T):
    X, R, C = map(int, input().split())
    if (R*C)%X != 0:
        print("Case #%d: RICHARD" % (t+1))
    else:
        if X-1 > R or X-1 > C:
            print("Case #%d: RICHARD" % (t+1))
        else:
            print("Case #%d: GABRIEL" % (t+1))
