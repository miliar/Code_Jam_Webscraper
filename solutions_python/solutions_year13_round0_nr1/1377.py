FIRST_PLAYER = "X won"
SECOND_PLAYER = "O won"
DRAW = "Draw"
GOING = "Game has not completed"

W = 1
L = 0
N = -1
ans = { (W,L): FIRST_PLAYER,
        (L,W): SECOND_PLAYER,
        (W,N): FIRST_PLAYER,
        (N,W): SECOND_PLAYER,
        (L,L): DRAW,
        (N,N): GOING,}

def check(raw_grid,p):
    grid = raw_grid.replace("T",p)
    win=p*4
    # rows:
    for i in range(4):
        row = grid[i*4:i*4 + 4]
        if row == win:
            return W
    
    # cols:
    for i in range(4):
        col = grid[i::4]
        if col == win:
            return W

    # diags:
    if grid[::5]==win:
        return W

    if grid[3:13:3]==win:
        return W

    if "." in grid:
        return N

    return L

f_in = open("input.txt")
f_out = open("output.txt","+w")
n = int(f_in.readline())
i = 0
while(i<n):
    i += 1
    l = f_in.readline()[:-1] + \
        f_in.readline()[:-1] + \
        f_in.readline()[:-1] + \
        f_in.readline()[:-1]
    f_in.readline()
    
    lo = l.replace("T","O")
    lx = l.replace("T","X")

    result_o = check(lo,"O")
    result_x = check(lx,"X")

    print("Case #" + str(i) + ": " + ans[result_x,result_o])

    
    #grid = Grid()
    f_out.write("Case #" + str(i) + ": " + ans[result_x,result_o] +"\n")


f_in.close()
f_out.close()
