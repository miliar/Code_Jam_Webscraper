casos = int(input())

for casoactual in range(casos):
    X,R,C = [int(i) for i in input().split()]
    if X >= 7:
        print('Case #' + str(casoactual+1) + ': RICHARD')
    else:
        if X > R and X > C:
            print('Case #' + str(casoactual+1) + ': RICHARD')
        elif X - 1 > R or X - 1 > C:
            print('Case #' + str(casoactual+1) + ': RICHARD')
        elif (R*C) % X != 0:
            print('Case #' + str(casoactual+1) + ': RICHARD')
        else:
            print('Case #' + str(casoactual+1) + ': GABRIEL')
