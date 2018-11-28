space_found = False

def check_case(board):
    winners = []
    for y in range(4):
        winner = check_line(board[y])
        if winner in "XO":
            return "%s won" % winner
        winners.append(winner)
    for x in range(4):
        line = [board[y][x] for y in range(4)]
        winner = check_line([board[y][x] for y in range(4)])
        if winner in "XO":
            return "%s won" % winner
        winners.append(winner)
    winner = check_line([board[a][a] for a in range(4)])
    if winner in "XO":
        return "%s won" % winner
    winners.append(winner)
    winner = check_line([board[a][3-a] for a in range(4)])
    if winner in "XO":
        return "%s won" % winner
    winners.append(winner)
    if "." in winners:
        return "Game has not completed"
    else:
        return "Draw"
            
def check_line(line):
    current = line[0]
    if current == '.':
        return current
    for char in line[1:]:
        if char == '.':
            return char
        elif char == 'T':
            continue
        else:
            if current == 'T':
                current = char
            elif current != char:
                return '/'
    return current
    
file = open("input.txt", "r")
num_cases = file.readline()
board = []
count = 1
for line in file:
    if len(line) == 1:
        print "Case #%d: %s" %(count, check_case(board))
        board = []
        count += 1
        continue
    board.append(line[:4])
    