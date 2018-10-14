def richardWins(X, R, C):
    if (R * C) % X != 0:
        return True

    if X > max(R, C):
        return True

    if X >= 7:
        return True

    a = int((X + 1) / 2)
    b = X - a + 1

    if min(a, b) > min(R, C):
        return True

    if (min(R, C) > 1) and (X >= 2 * min(R, C)):
        return True

    return False


T = int(input())

for i in range(1, T + 1):
    
    X, R, C = [int(s) for s in input().split()]
    
    print("Case #", i, ": ", ('RICHARD' if richardWins(X, R, C) else 'GABRIEL'), sep='')


