import sys

status = [
    "X won",
    "O won",
    "Draw",
    "Game has not completed",
]

def check_four(data):
    tc_status = None
    count = 0
    first = False
    for x in range(0,4):
        current = data[x]
        if current == '.':
            tc_status = status[3] 
            break
        elif current == 'T':
            count += 1
        elif not first:
            count += 1
            first = current 
        elif first == current:
            count += 1
        else:
            break
    if count == 4:
        if first == 'X':
            tc_status = status[0]
        elif first == 'O':
            tc_status = status[1]
        else:
            raise Exception("No winner but count == 4: {}".format(first))
    return tc_status

def check_board(tc):
    tc_status = None
    # Check diagonals
    diagonals = [
        [tc[0][0], tc[1][1], tc[2][2], tc[3][3]],
        [tc[0][3], tc[1][2], tc[2][1], tc[3][0]],
    ]
    # Check diagonals
    for i in range(2):
        tc_status = check_four(diagonals[i])
        if tc_status and tc_status != status[3]:
            return tc_status
    # Check rows and columns
    for i in range(2):
        for j in range(0,4):
            # Check rows
            if i == 0:
                data = [tc[j][x] for x in range(0,4)]
                tc_status = check_four(data)
            # Check columns
            else:
                data = [tc[y][j] for y in range(0,4)]
                tc_status = check_four(data)
            if tc_status and tc_status != status[3]:
                return tc_status
    if not tc_status:
        tc_status = status[2]
    return tc_status

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    T = int(lines[0])
    test_data = []
    counter = 1
    for i in range(T):
        data = []
        for j in range(4):
            data.append([c for c in lines[counter+j]])
        counter += 5
        test_data.append(data)
    for i in range(T):
        print("Case #{}: {}".format(i + 1, check_board(test_data[i])))
