
def check(line, player):
    for entry in line:
        if not entry == "T" and not entry == player:
            return False
    return True

def solve(table):
    # Check rows
    for row in range(4):
        line = table[row*4:row*4+4]
        if check(line, "O"):
            return "O"
        elif check(line, "X"):
            return "X"
    # Check columns
    for column in range(4):
        line = table[column::4]
        if check(line, "O"):
            return "O"
        elif check(line, "X"):
            return "X"
    # Diagonal
    line = [table[i*4+i] for i in range(4)]
    if check(line, "O"):
        return "O"
    elif check(line, "X"):
        return "X"

    line = [table[r*4+c] for r, c in zip(range(4), range(3, -1, -1))]
    if check(line, "O"):
        return "O"
    elif check(line, "X"):
        return "X"
    if "." in table:
        return
    return "DRAW"

if __name__ == "__main__":
    cases = int(raw_input())
    for case in range(cases):
        table = []
        for i in range(4):
            table.extend(raw_input())
        raw_input()
        result = solve(table)
        print "Case #%d:" % (case + 1),
        if result == "X":
            print "X won"
        elif result == "O":
            print "O won"
        elif result == "DRAW":
            print "Draw"
        elif not result:
            print "Game has not completed"
