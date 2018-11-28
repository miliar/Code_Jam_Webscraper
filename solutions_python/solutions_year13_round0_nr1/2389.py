import sys

def equal(a, b, c, d):
    if (a == 'X' or a == 'T') and (b == 'X' or b == 'T') and (c == 'X' or c == 'T') and (d == 'X' or d == 'T'):
        return 'X'
    if (a == 'O' or a == 'T') and (b == 'O' or b == 'T') and (c == 'O' or c == 'T') and (d == 'O' or d == 'T'):
        return 'O'
    return None

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    for tc in range(n):
        a = []
        for j in range(5):
            s = sys.stdin.readline().strip()
            a.append(s)
        is_ended = True
        for i in range(4):
            for j in range(4):
                if (a[i][j] == '.'):
                    is_ended = False
        res = "Draw" if is_ended else "Game has not completed"
        for i in range(4):
            r = equal(a[i][0], a[i][1], a[i][2], a[i][3])
            if (r):
                res = r + " won"
            r = equal(a[0][i], a[1][i], a[2][i], a[3][i])
            if (r):
                res = r + " won"
        r = equal(a[0][0], a[1][1], a[2][2], a[3][3])
        if (r):
            res = r + " won"
        r = equal(a[0][3], a[1][2], a[2][1], a[3][0])
        if (r):
            res = r + " won"
        print "Case #" + str(tc + 1) + ": " + res