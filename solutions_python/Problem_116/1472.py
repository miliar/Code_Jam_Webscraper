def win(m, c):
    ma = [r.replace("T",c) for r in m]
    for i in range(4):
        if ma[i][0] == ma[i][1] == ma[i][2] == ma[i][3] == c:
            return True
        if ma[0][i] == ma[1][i] == ma[2][i] == ma[3][i] == c:
            return True

    if all(ma[i][i] == ma[i+1][i+1] == c for i in range(3)): return True
    if all(ma[3-i][i] == ma[3-i-1][i+1] == c for i in range(3)): return True
    return False

start = False # X
n = int(raw_input())
for i in range(n):
    m = [raw_input() for r in range(4)]
    if i != n-1: raw_input()

    w = [win(m,"X"), win(m,"O")]
    r = "Case #{0}: ".format(i+1)
    if all(w): r += "XO"[start] + " won"
    elif any(w): r += "XO"[w.index(True)] + " won"
    elif any(['.' in s for s in m]):  r+=  "Game has not completed"
    else: r+= "Draw"
    print r
    start = not start
