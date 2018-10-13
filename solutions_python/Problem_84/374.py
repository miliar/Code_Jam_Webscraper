import sys

if __name__ == '__main__':
    imp = "Impossible"

    f = sys.stdin
    if len(sys.argv) >= 2:
        f = open(sys.argv[1])

    board = []
    h, w = 0, 0

    n = int(f.readline())

    for i in range(n):
        h, w = 0, 0
        board = []
        out = ""
        h, w = map(int, f.readline().split())

        s = 0
        for j in range(h):
            l = list(str.strip(f.readline()))
            board.append(l)
            s += len(filter(lambda x: x == "#", l))

        if s % 4 != 0:
            out = imp
        else:
            for y in range(h-1):
                for x in range(w-1):
                    if board[y][x] == "#":
                        if [board[y][x+1], board[y+1][x], board[y+1][x+1]] == ["#","#","#"]:
                                board[y][x+1] = "\\"
                                board[y+1][x] = "\\"
                                board[y][x] = "/"
                                board[y+1][x+1] = "/"

            out = "\n".join(map(lambda x: "".join(x), board))
            for y in range(h):
                for x in range(w):
                    if board[y][x] == "#":
                        out = imp
                        break

        print "Case #%d:\n%s" % (i+1, out)

    f.close()
