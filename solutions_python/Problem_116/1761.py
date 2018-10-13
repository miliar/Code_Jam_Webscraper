import sys

def update(f, count_x, count_o):
    if f == 'X':
        count_x += 1
    elif f == 'O':
        count_o += 1
    elif f == 'T':
        count_o += 1
        count_x += 1

    return count_x, count_o

def get_status(field):
    max_x = 0
    max_o = 0
    count_points = 0
    N = len(field)

    # check rows
    for row in range(N):
        count_x = 0
        count_o = 0
        for col in range(N):
            if field[row][col] == '.':
                count_points += 1
            count_x, count_o = update(field[row][col], count_x, count_o)

        max_x = max(max_x, count_x)
        max_o = max(max_o, count_o)

    # check cols
    for col in range(N):
        count_x = 0
        count_o = 0
        for row in range(N):
            count_x, count_o = update(field[row][col], count_x, count_o)

        max_x = max(max_x, count_x)
        max_o = max(max_o, count_o)

    # check diaognals
    count_x1, count_o1 = 0, 0
    count_x2, count_o2 = 0, 0
    for i in range(N):
        count_x1, count_o1 = update(field[i][i], count_x1, count_o1)
        count_x2, count_o2 = update(field[i][N - 1 - i], count_x2, count_o2)

    max_x = max(max_x, count_x1, count_x2)
    max_o = max(max_o, count_o1, count_o2)

    if max_x == 4 and max_o < 4:
        return "X won"
    elif max_o == 4 and max_x < 4:
        return "O won"
    elif max_x == 4 and max_o == 4:
        return "Draw"
    elif count_points > 0:
        return "Game has not completed"
    else:
        return "Draw"

if __name__ == "__main__":
    num_testcases = int(sys.stdin.readline())
    for i in range(1, num_testcases+1):
        field = []
        for j in range(4):
            field.append([x for x in sys.stdin.readline()])
        print("Case #{n}: {result}".format(n=i, result=get_status(field)))
        sys.stdin.readline()