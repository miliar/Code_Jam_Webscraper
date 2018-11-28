from pprint import pprint

def tictactoe(mat): # UGLY
    res = set()
    # check diags
    if mat[0][0] == mat[1][1] and mat[1][1] == mat[2][2] and mat[2][2] == mat[3][3]:
        if mat[0][0] != ".":
            res.add(mat[0][0])
    if mat[0][3] == mat[1][2] and mat[1][2] == mat[2][1] and mat[2][1] == mat[3][0]:
        if mat[0][3] != ".":
            res.add(mat[0][3])
    # check lines and cols
    for i in range(4):
        if mat[i][0] == mat[i][1] and mat[i][1] == mat[i][2] and \
           mat[i][2] == mat[i][3]:
            if mat[i][0] != ".":
                res.add(mat[i][0])
        if mat[0][i] == mat[1][i] and mat[1][i] == mat[2][i] and \
           mat[2][i] == mat[3][i]:
            if mat[0][i] != ".":
                res.add(mat[0][i])
    return res

def tictactomek(mat):
    ti, tj = (-1, -1)
    tingame = False
    emptys = 0
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 'T':
                tingame = True
                ti, tj = i, j
            if mat[i][j] == '.':
                emptys += 1
    res = set()
    if tingame:
        mat[ti][tj] = "O"
        res = tictactoe(mat)
        mat[ti][tj] = "X"
        res = res.union(tictactoe(mat))
    else:
        res = tictactoe(mat)
    if "X" in res and "O" in res:
        return "Draw"
    if len(res) == 0 and emptys == 0:
        return "Draw"
    if len(res) == 0:
        return "Game has not completed"
    if "X" in res:
        return "X won"
    if "O" in res:
        return "O won"
    return None

def printres(i, res):
    print("Case #%d: %s" % (i, res))

def main():
    import sys
    mat = []
    i = 0
    for line in sys.stdin:
        if i == 0:
            i += 1
            continue
        sline = line.strip()
        if sline:
            mat.append(list(sline))
        if len(mat) == 4:
            printres(i, tictactomek(mat))
            i += 1
            mat = []


if __name__ == "__main__":
    main()
