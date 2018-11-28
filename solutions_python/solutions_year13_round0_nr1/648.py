import sys


def solve(instream):
    board = [instream.readline().strip() for x in range(4)]
    instream.readline()

    for ch in ("X", "O"):
        won = False
        for row in range(4):
            won = won or all(x in (ch, "T") for x in board[row])

        for col in range(4):
            won = won or all(x[col] in (ch, "T") for x in board)

        won = won or all(board[i][i] in (ch, "T") for i in range(4))
        won = won or all(board[3 - i][i] in (ch, "T") for i in range(4))
        if won:
            return "{} won".format(ch)

    completed = all([all(cell != "." for cell in row) for row in board])
    if completed:
        return "Draw"
    else:
        return "Game has not completed"

def run():
    cases = int(sys.stdin.readline().strip())
    for i in range(cases):
        print("Case #{}: {}".format(i + 1, solve(sys.stdin)))

if __name__ == "__main__":
    run()
