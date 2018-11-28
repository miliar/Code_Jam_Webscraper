T = int(input())

for CC in range(T):

    X, R, C = map(int,input().split())
    Ans = None

    if X == 1:
        Ans = True
    elif X == 2:
        if R*C%2 == 0:
            Ans = True
        else:
            Ans = False
    elif X == 3:
        if R*C%3 == 0:
            minrc = min(R,C)
            if 1 <= minrc <= 1:
                Ans = False
            else:
                Ans = True
        else:
            Ans = False
    elif X == 4:
        if R*C%4 == 0:
            minrc = min(R,C)
            if 1 <= minrc <= 2:
                Ans = False
            else:
                Ans = True
        else:
            Ans = False
    


    if Ans == True:
        Ans = 'GABRIEL'
    elif Ans == False:
        Ans = 'RICHARD'
        
    print('Case #{}: {}'.format(CC+1,Ans))
