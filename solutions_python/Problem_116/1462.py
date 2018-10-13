def solve():
    b = [input() for _ in range(5)]

    dif = [(i, j) for i in range(-1,2) for j in range(-1, 2) if i or j]


    dot = False
    for i in range(4):
        for j in range(4):
            if b[i][j] == '.':
                dot = True
            for k in range(len(dif)):
                pos = [(i + dif[k][0] * l, j + dif[k][1] * l) for l in range(4)]                
                if pos[-1] in [(x,y) for x in range(0, 4) for y in range(0, 4)]:
                    for c in "OX":
                        if(len([p for p in pos if b[p[0]][p[1]] in "T" + c]) == 4):
                            return c + " won"

    if dot:
        return "Game has not completed"
    else:
        return "Draw"


T = int(input())
for tn in range(T):
    print("Case #{0}: {1}".format(tn + 1, solve()))
    

