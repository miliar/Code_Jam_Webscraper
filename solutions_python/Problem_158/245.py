for T in range(int(input())):
    X, R, C = map(int,input().split())
    Anterior = True
    if X >= 7:
        Anterior = False
    elif X > R and X > C:
        Anterior = False
    elif R * C % X != 0:
        Anterior = False
    elif (X + 1) // 2 > min(R, C):
        Anterior = False
    elif X in (1, 2, 3):
        Anterior = True
    elif X == 4:
        Anterior = min(R, C) > 2
    elif X == 5:
        Anterior = not(min(R, C) == 3 and max(R, C) == 5)
    elif X == 6:
        Anterior = min(R, C) > 3
    print('Case #%d:' % (T + 1), 'GABRIEL' if Anterior else 'RICHARD')