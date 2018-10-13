lines = open("large.in", "rU").read().split("\n\n")
lines[0] = "\n".join(lines[0].split("\n")[1:])

change = [(0, 1), (1, 0), (1, -1), (1, 1)]


def test(board, x, y, dx, dy):
    if 0 <= x + (dx * 3) <= 3 and 0 <= y + (dy * 3) <= 3:
        x -= dx
        y -= dy
        counts = {}
        for i in xrange(4):
            x += dx
            y += dy
#            print board, x, y
            counts[board[y][x]] = counts.get(board[y][x], 0) + 1
        if counts.get("T", 0) + counts.get("X", 0) == 4:
            return "X"
        elif counts.get("T", 0) + counts.get("O", 0) == 4:
            return "O"


for (i, board) in enumerate(lines):
    winners = {"X": 0, "O": 0, None: 0}
    board = board.split("\n")[:4]
    for dx, dy in change:
        for y in xrange(4):
            for x in xrange(4):
                winners[test(board, x, y, dx, dy)] += 1
    print "Case #%d:" % (i+1),
    if winners["X"] and winners["O"]:
        print "Draw"
    elif winners["X"]:
        print "X won"
    elif winners["O"]:
        print "O won"
    else:
        if "." in "".join(board):
            print "Game has not completed"
        else:
            print "Draw"
