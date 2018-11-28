import sys

file = sys.argv[1]
text = open(file)
lines = text.readlines()

cases = lines.pop(0);


"""
    Returns:       
        0 if x won
        1 if O won
        2 if game has not completed
        3 if draw
"""
def analyse_row(row):
    if '.' in row:
        return 2
    if 'X' in row and 'O' in row:
        return 3
    if 'X' not in row and '.' not in row:
        return 1
    return 0

def analyse_4rows(row1, row2, row3, row4):
    result_rows = [analyse_row(row1), analyse_row(row2), analyse_row(row3), analyse_row(row4)]
    if 0 in result_rows:
        return 0
    if 1 in result_rows:
        return 1
    if 2 in result_rows:
        return 2
    return 3


def diagonal(row1, row2, row3, row4):
    d1 = row1[0]+row2[1]+row3[2]+row4[3]
    d2 = row1[3]+row2[2]+row3[1]+row4[0]
    if ('X' not in d1 and '.' not in d1) or ('X' not in d2 and '.' not in d2):
        return 1
    if ('O' not in d1 and '.' not in d1) or ('O' not in d2 and '.' not in d2):
        return 0 
    if '.' in d1 or '.' in d2:
        return 2
    return 3


def analyse_game(row1, row2, row3, row4):
    game_result = [analyse_4rows(row1, row2, row3, row4),]
    cols = transpose(row1, row2, row3, row4)
    game_result.append(analyse_4rows(cols[0], cols[1], cols[2], cols[3]))
    game_result.append(diagonal(row1, row2, row3, row4))
    if 0 in game_result:
        return 0
    if 1 in game_result:
        return 1
    if 2 in game_result:
        return 2
    return 3


def transpose(row1, row2, row3, row4):
    col = ["", "", "", ""]
    for i in range(4):
        col[i] = row1[i]+row2[i]+row3[i]+row4[i]
    return (col[0], col[1], col[2], col[3])

def main():
    for i in range(int(cases)):
        result = analyse_game(str(lines.pop(0)), str(lines.pop(0)), str(lines.pop(0)), str(lines.pop(0)))
        if len(lines)>0:
            lines.pop(0)
        if result == 0:
            statement = "X won"
        elif result == 1:
            statement = "O won"
        elif result == 2:
            statement = "Game has not completed"
        else:
            statement = "Draw"
        if i == int(cases):
            print("Case #{0}: {1}".format(i+1, statement), end="")
        print("Case #{0}: {1}".format(i+1, statement), end="\n")
main()