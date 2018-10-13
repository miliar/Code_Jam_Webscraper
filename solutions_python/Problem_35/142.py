import sys

def go(r, c, cur, mm, bb, w, h, move):
    if bb[r][c] > 0: return bb[r][c]

    r2 = -1
    c2 = -1
    for i in range(0, 4):
        rr = r + move[i][0]
        cc = c + move[i][1]
        if rr >= 0 and rr < h and cc >= 0 and cc < w and mm[rr][cc] < mm[r][c]:
            if r2 < 0 or mm[rr][cc] < mm[r2][c2]:
                r2 = rr
                c2 = cc
    if r2 >= 0:
        bb[r][c] = go(r2, c2, cur, mm, bb, w, h, move)
        return bb[r][c]

    bb[r][c] = cur
    return cur

def main():
    ca = 0
    move = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    with open("B-large.in", "r") as cin:
        T = int(cin.readline())
        for t in range(0, T):
            tokens = cin.readline().split()
            h = int(tokens[0])
            w = int(tokens[1])
            bb = []
            for i in range(0, h):
                bb.append([])
                for j in range(0, w):
                    bb[i].append(0)
            mm = []
            for i in range(0, h):
                tokens = cin.readline().split()
                mm.append([])
                for j in range(0, w):
                    mm[i].append(int(tokens[j]))

            cur = ord('a')
            for i in range(0, h):
                for j in range(0, w):
                    if bb[i][j] == 0:
                        if cur == go(i, j, cur, mm, bb, w, h, move):
                            cur += 1

            ca += 1
            print "Case #%d:" % (ca)
            for i in range(0, h):
                for j in range(0, w):
                    if j > 0: sys.stdout.write(' ')
                    sys.stdout.write(chr(bb[i][j]))
                sys.stdout.write('\n')

if __name__ == "__main__":
    main()
