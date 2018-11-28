import sys
import pprint


def process_input(input):
    result = []
    lines = list(input)[:-1]
    while lines:
        result.append(list(reversed([lines.pop().strip() for _ in range(4)])))
        lines.pop()
    result.reverse()
    return result


def generate_possibilites(block):
    return [ tuple(e) for e in block]+\
        zip(*block) +\
        [ tuple(block[e][e] for e in range(len(block)))] +\
        [ tuple(block[e][3 - e] for e in range(len(block)))]


def winner_search(block):

    for possibility in generate_possibilites(block):
        x_won = "".join(possibility).replace("T", "X")
        if x_won == "XXXX":
            return "X won"

        o_won = "".join(possibility).replace("T", "O")
        if o_won == "OOOO":
            return "O won"

    if "." in "".join(block):
        return "Game has not completed"

    return "Draw"


for i, block in enumerate(process_input(sys.stdin), 1):
    print "Case #%s: %s" % (i, winner_search(block))
