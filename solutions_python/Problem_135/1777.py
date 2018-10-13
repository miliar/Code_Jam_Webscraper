def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

def game(l):
    return (l[0][0] - 1, l[1:5], l[5][0] - 1, l[6:])

def play(i, (row1, board1, row2, board2)):
    i += 1
    intr = set(board1[row1]) & set(board2[row2])
    if not len(intr):
        return "Case #{}: Volunteer cheated!".format(i)
    elif len(intr) == 1:
        return "Case #{}: {}".format(i, intr.pop())
    else:
        return "Case #{}: Bad magician!".format(i)

f = open("A-small-attempt0.in", "r")
contents = filter(lambda l: len(l) > 0, f.read().split("\n"))
contents = map(lambda l: map(int, l.split()), contents)
boards = map(lambda l: map(lambda x: list(x), l), list(chunks(contents[1:], 10)))
boards = map(lambda b: play(*b), enumerate(map(game, boards)))

print "\n".join(boards)
