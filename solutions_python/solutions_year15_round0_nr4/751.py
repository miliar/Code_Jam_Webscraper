cases = int(input())

for case in range(cases):
    x, r, c = map(int, input().split(' '))

    richard = False
    #covers 1 & 2: the board doesn't have the same # of squares
    if r*c % x != 0:
        richard = True
    elif x < 3:
        richard = False
    #covers 3 & 4: above and an L in a thin space
    elif r < 2 or c < 2:
        richard = True
    #covers 4: S in small space (trapped square)
    elif x == 4 and r < 3 and c < 3:
        richard = True
    elif x == 4 and ((r == 4 and c == 2) or (c == 4 and r == 2)):
        richard = True
    

    winner = "RICHARD" if richard else "GABRIEL"
    print("Case #{}: {}".format(case+1, winner))
