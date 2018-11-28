# ominous omino

infile = open('D-small-attempt2.in', 'rU')
outfile = open('D-small.out', 'w')

gabe = "GABRIEL"
rich = "RICHARD"  # i.e. can't fit

num_cases = int(infile.readline())
for cur_case in range(1, num_cases + 1):
    # do stuff
    x, rows, cols = map(int, infile.readline().split())

    # basic bounds test for things
    if x > rows and x > cols:
        winner = rich
    elif rows * cols < x:
        winner = rich
    elif (rows * cols) % x != 0:
        winner = rich
    elif x > rows * 2 or x > cols * 2:
        # case where a certain shape is chosen that doesn't fit
        # basically, dimensions always fulfil length + height = x
        winner = rich
    elif x == 4 and (rows <= 2 or cols <= 2):
        # the shape blocks off the path
        winner = rich
    else:
        winner = gabe

    print("Case #{}: {}".format(cur_case, winner))
    outfile.write("Case #{}: {}\n".format(cur_case, winner))

infile.close()
outfile.close()
