from __future__ import division


def reader(in_file):
    r,c = in_file.get_ints()
    board = []
    for _ in xrange(r):
        board.append(in_file.readline())
    return r,c,board


def get(b):
    for c in b:
        if c != "?":
            return c


def solver((r, c, board)):
    first_with_thing = -1
    for i, row in enumerate(board):
        if row != "?" * c:
            first_with_thing = i
            break
    latest_line = ""
    for j in xrange(first_with_thing, r):
        if board[j] == "?" * c:
            board[j] = latest_line
            continue
        firstnon = get(board[j])
        build_line = ""
        for char in board[j]:
            if char == "?":
                build_line += firstnon
            else:
                build_line += char
                firstnon = char
        board[j] = build_line
        latest_line = build_line

    for i in xrange(0, first_with_thing):
        board[i] = board[first_with_thing]

    return "\n" + "\n".join(board)


if __name__ == "__main__":
    # GCJ library publicly available at http://ideone.com/2PcmZT
    from GCJ import GCJ
    GCJ(reader, solver, "a", "A").run()
