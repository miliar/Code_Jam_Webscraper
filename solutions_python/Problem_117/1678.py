import sys

def check(game):
    # For each row
    for row in range(len(game)):
        # Find minimum and maximum
        min_h = min(game[row])
        max_h = max(game[row])
        # If equal the height is uniform => no problem
        if min_h != max_h:
            # The column where there is a minimum has to be uniform
            for col, h in enumerate(game[row]):
                if h == min_h:
                    min_h_col = min([game[row][col] for row in range(len(game))])
                    max_h_col = max([game[row][col] for row in range(len(game))])
                    if max_h_col != min_h_col:
                        return "NO"
    return "YES"

data = sys.stdin

# Reading number of cases
n = int(data.readline())

for t in range(n):
    # Reading size
    m, n = data.readline().split(' ')
    # Reading 4 lines
    game = []
    for row in range(int(m)):
        game.append([int(c) for c in data.readline()[:-1] if c != ' '])

    # Checking
    print "Case #%d:"%(t+1), check(game)

