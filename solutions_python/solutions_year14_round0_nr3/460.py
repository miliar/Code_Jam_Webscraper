import math

IMPOSSIBLE = "Impossible"


def result(R, C, M):
    empty = R * C - M

    # universal special cases
    # no empty spaces
    if empty == 0:
        return IMPOSSIBLE
    # one empty space, under the first clicked square
    if empty == 1:
        board = [["*"] * C for i in range(R)]
        board[0][0] = "c"
        return format_board(board)

    # simple special cases of very small boards
    # 1x1, 2x1, 1x2, 2x2 (all empty)
    if R == 1 and C == 1 and M == 0:
        return "c"
    if R == 2 and C == 1 and M == 0:
        return "c\n."
    if R == 1 and C == 2 and M == 0:
        return "c."
    if R == 2 and C == 2 and M == 0:
        return "c.\n.."

    # special case of 1xn
    if R == 1:
        if empty >= 2:
            return "c" + "."*(empty-1) + "*"*M
        else:
            return IMPOSSIBLE

    # special case of nx1
    if C == 1:
        if empty >= 2:
            return "c\n" + ".\n"*(empty-1) + "\n".join(["*"]*M)
        else:
            return IMPOSSIBLE

    # # special case of 2xn
    # if R == 2:
    #     if empty >= 4 and M % 2 == 0:
    #         return "c"

    # special case of nx2

    # rest of code works for 3x3 and larger!

    # check impossible sizes
    if empty <= 0 or empty in [2, 3, 5, 7]:
        return IMPOSSIBLE

    # empty board
    board = [["."] * C for i in range(R)]

    # always click in upper left corner
    board[0][0] = "c"

    # special cases of large boards
    if empty == 4:
        for y in range(R):
            for x in range(C):
                if not (y < 2 and x < 2):
                    board[y][x] = "*"
    elif empty == 6:
        for y in range(R):
            for x in range(C):
                if C > 2:
                    if not (y < 2 and x < 3):
                        board[y][x] = "*"
                else:
                    if not (y < 3 and x < 2):
                        board[y][x] = "*"
    else:
        # fill board from lower right
        for y in range(2, R):
            for x in range(2, C):
                if (R-y-1) * (C-2) + (C-x) <= M:
                    board[y][x] = "*"

        remaining = max(0, M - (R-2)*(C-2))

        gutter_count = math.ceil(remaining/2.0)

        # fill in gutters from bottom
        for y in range(max(3, R-gutter_count), R):
            board[y][0] = board[y][1] = "*"

        # fill in gutters from right
        # (second max function handles the R==2 case)
        for x in range(max(3, C-(gutter_count-max((R-3),0))), C):
            board[0][x] = board[1][x] = "*"

        # remove the (3,3) mine if M is odd and gutters are used
        # if it can't be removed since the board has height/width of 2, board is impossible
        if gutter_count > 0 and remaining % 2 == 1:
            if R > 2 and C > 2:
                board[2][2] = "."
            else:
                return IMPOSSIBLE

    return format_board(board)

def format_board(board):
    return "\n".join(["".join(row) for row in board])

def main():
    with open('C.in') as f:
        with open('C.out', 'w') as f2:
            lines = list(f.readlines())[1:]
            for i, line in enumerate(lines):
                nums = [int(num) for num in line.split(" ")]
                output = result(*nums)
                # print(output.count("*") == nums[2] or output == IMPOSSIBLE)
                if output == IMPOSSIBLE:
                    print(i+1, nums, nums[0]*nums[1]-nums[2])
                output = "Case #" + str(i+1) + ":\n" + output
                if output[-1] != "\n":
                    output += "\n"
                f2.write(output)

main()