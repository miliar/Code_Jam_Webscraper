import Solve

def checkWin(l, c):
    cols=["","","", ""]
    for s in l:
        for i in range(len(s)):
            cols[i] += s[i]
        if s.count(c) >= 4:
            return True
    for s in cols:
        if s.count(c) >= 4:
            return True
    print l
    return l[0][0] == l[1][1] == l[2][2] == c or l[0][3] == l[3][0] == l[2][1] == l[1][2] == c

def tttt(args):
    notComp = False
    lo = []
    lx = []
    for s in args[:4]:
        if s.count(".") > 0: notComp = True
        lo.append(s.replace("T", "O"))
        lx.append(s.replace("T", "X"))
    wo = checkWin(lo, "O")
    wx = checkWin(lx, "X")
    if wo: return "O won"
    if wx: return "X won"
    if notComp: return "Game has not completed"
    return "Draw"

if __name__ == "__main__":
    Solve.solve("A-small-attempt0.in", "A.txt", tttt, 5)
