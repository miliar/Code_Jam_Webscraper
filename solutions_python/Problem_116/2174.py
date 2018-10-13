import re

def find_winner(game):
    lines = [x.strip() for x in game.split("\n") if x.strip()]

    x = 0
    while x < 4:
        lines.append( "%s%s%s%s" % (lines[0][x], lines[1][x], lines[2][x], lines[3][x]) )
        x += 1

    # diagonal
    lines.append( "%s%s%s%s" % (lines[0][0], lines[1][1], lines[2][2], lines[3][3]) )
    lines.append( "%s%s%s%s" % (lines[0][3], lines[1][2], lines[2][1], lines[3][0]) )

    for l in lines:
        if re.match(r"(x|t){4}", l, re.I):
            return "X won"
        elif re.match(r"(o|t){4}", l, re.I):
            return "O won"

    if "." in game:
        return "Game has not completed"
    else:
        return "Draw"


T = int(raw_input())
X = 1
while T > 0:
    game = "%s\n%s\n%s\n%s%s" % (raw_input(),raw_input(),raw_input(),raw_input(),raw_input())
    print "Case #%d: %s" % (X, find_winner(game))
    T -= 1
    X += 1

