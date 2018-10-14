import sys,functools

lines = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for x in range(0,4):
    for y in range(0,4):
        lines[x][y] = [x,y+4]+([8] if x == y else ([9] if x+y == 3 else []))
f = open(sys.argv[1],'r')
n = int(next(f))

def test_board():
    X = [True for x in range(0,10)]
    O = [True for x in range(0,10)]

    full = True

    for x in range(0,4):
        for y in range(0,4):
            if(board[x][y] == "."): full = False
            if(board[x][y] != "T"):
                if(board[x][y] != "X"):
                    for l in lines[x][y]:
                        X[l] = False
                if(board[x][y] != "O"):
                    for l in lines[x][y]:
                        O[l] = False
    if(functools.reduce((lambda x,y: x or y), X)): return "X won"
    if(functools.reduce((lambda x,y:x or y), O)): return "O won"
    if(full): return "Draw"
    return "Game has not completed"

for i in range(0,n):
    for j in range(0,4): board[j] = next(f)[:-1]
    print("Case #%d: %s"%(i+1,test_board()))
    try: 
        next(f)
    except:
        pass
