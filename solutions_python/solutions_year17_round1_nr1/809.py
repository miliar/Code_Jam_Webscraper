debug = False

def check_row(cakes, row, sc, ec, val):
    for i in range(sc, ec + 1):
        if cakes[row][i] != "" and val == "":
            val = cakes[row][i]
        elif cakes[row][i] == "":
            continue
        elif cakes[row][i] != val:
            return False
    return True

def check_col(cakes, col, sr, er, val):
    for i in range(sr, er + 1):
        if cakes[i][col] != "" and val == "":
            val = cakes[i][col]
        elif cakes[i][col] == "":
            continue
        elif cakes[i][col] != val:
            return False
    return True

def give(cakes, finish, x, y):
    row = len(cakes)
    col = len(cakes[0])
    w = 1
    h = 1
    owner = cakes[x][y]

    #dia
    while x + h - 1 < row and y + w - 1 < col:
        col_pass = False
        row_pass = False

        if y + w < col:
            col_pass = check_col(cakes, y + w, x, x + h - 1, owner)
            if debug:
                print "check col {}.{} to {}.{} for {} and {}".format(x, y + w, x + h - 1, y + w, owner, col_pass)
            if col_pass:
                if owner == "":
                    for i in range(x, x + h):
                        if cakes[i][y + w] != "":
                            owner = cakes[i][y + w]
                            break
                w += 1

        if x + h < row:
            row_pass = check_row(cakes, x + h, y, y + w - 1, owner)
            if debug:
                print "check row {}.{} to {}.{} for {} and {}".format(x + h, y, x + h, y + w - 1, owner, row_pass)
            if row_pass:
                if owner == "":
                    if debug:
                        print "find owner from {}.{} to {}.{}".format(x, y, x, y + w - 1)
                    for i in range(y, y + w):
                        if cakes[x + h][i] != "":
                            owner = cakes[x + h][i]
                            break
                h += 1
        if not col_pass and not row_pass:
            break

    if owner == "":
        w = 1
        h = 1
        if debug:
            print "Round2"
        while x + h - 1 < row and y + w - 1 < col:
            col_pass = False
            row_pass = False

            if x + h < row:
                row_pass = check_row(cakes, x + h, y, y + w - 1, owner)
                if debug:
                    print "check row {}.{} to {}.{} for {} and {}".format(x + h, y, x + h, y + w - 1, owner, row_pass)
                if row_pass:
                    if owner == "":
                        if debug:
                            print "find owner from {}.{} to {}.{}".format(x + h, y, x + h, y + w - 1)
                        for i in range(y, y + w):
                            if cakes[x + h][i] != "":
                                owner = cakes[x + h][i]
                                break
                    h += 1

            if y + w < col:
                col_pass = check_col(cakes, y + w, x, x + h - 1, owner)
                if debug:
                    print "check col {}.{} to {}.{} for {} and {}".format(x, y + w, x + h - 1, y + w, owner, col_pass)
                if col_pass:
                    if owner == "":
                        if debug:
                            print "find owner from {}.{} to {}.{}".format(x, y + w, x + h - 1, y + w)
                        for i in range(x, x + h):
                            if cakes[i][y + w] != "":
                                owner = cakes[i][y + w]
                                break
                    w += 1
            if not col_pass and not row_pass:
                break
    if owner == "":
        w = 1
        h = 1
        if debug:
            print "Round3"
        while x + h - 1 < row:
            row_pass = False
            if x + h < row:
                row_pass = check_row(cakes, x + h, y, y + w - 1, owner)
                if debug:
                    print "check row {}.{} to {}.{} for {} and {}".format(x + h, y, x + h, y + w - 1, owner, row_pass)
                if row_pass:
                    if owner == "":
                        if debug:
                            print "find owner from {}.{} to {}.{}".format(x + h, y, x + h, y + w - 1)
                        for i in range(y, y + w):
                            if cakes[x + h][i] != "":
                                owner = cakes[x + h][i]
                                break
                    h += 1
            if not row_pass:
                break;

        while y + w - 1 < col:
            col_pass = False
            if y + w < col:
                col_pass = check_col(cakes, y + w, x, x + h - 1, owner)
                if debug:
                    print "check col {}.{} to {}.{} for {} and {}".format(x, y + w, x + h - 1, y + w, owner, col_pass)
                if col_pass:
                    if owner == "":
                        if debug:
                            print "find owner from {}.{} to {}.{}".format(x, y + w, x + h - 1, y + w)
                        for i in range(x, x + h):
                            if cakes[i][y + w] != "":
                                owner = cakes[i][y + w]
                                break
                    w += 1
            if not col_pass:
                break
    if owner == "":
        w = 1
        h = 1
        if debug:
            print "Round4"
        while y + w - 1 < col:
            col_pass = False
            if y + w < col:
                col_pass = check_col(cakes, y + w, x, x + h - 1, owner)
                if debug:
                    print "check col {}.{} to {}.{} for {} and {}".format(x, y + w, x + h - 1, y + w, owner, col_pass)
                if col_pass:
                    if owner == "":
                        if debug:
                            print "find owner from {}.{} to {}.{}".format(x, y + w, x + h - 1, y + w)
                        for i in range(x, x + h):
                            if cakes[i][y + w] != "":
                                owner = cakes[i][y + w]
                                break
                    w += 1
            if not col_pass:
                break
        while x + h - 1 < row:
            row_pass = False
            if x + h < row:
                row_pass = check_row(cakes, x + h, y, y + w - 1, owner)
                if debug:
                    print "check row {}.{} to {}.{} for {} and {}".format(x + h, y, x + h, y + w - 1, owner, row_pass)
                if row_pass:
                    if owner == "":
                        if debug:
                            print "find owner from {}.{} to {}.{}".format(x + h, y, x + h, y + w - 1)
                        for i in range(y, y + w):
                            if cakes[x + h][i] != "":
                                owner = cakes[x + h][i]
                                break
                    h += 1
            if not row_pass:
                break;


    for i in range(x, x + h):
        for j in range(y, y + w):
            cakes[i][j] = owner
    finish.append(owner)

def print_cakes(cakes, finish):
    for i in range(0, len(cakes)):
        out = ""
        for j in range(0, len(cakes[0])):
            if cakes[i][j] == "":
                out = out + " "
            else:
                out = out + cakes[i][j]
        print out
    if debug:
        print finish
        print ""


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    row, col = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case

    cakes = []
    for j in range(0, row):
        raw_row = list(raw_input())
        for x in range(0, col):
            if raw_row[x] == "?":
                raw_row[x] = ""
        cakes.append(raw_row)
    finish = []

    for x in range(0, row):
        for y in range(0, col):
            if cakes[x][y] == "" or cakes[x][y] not in finish:
                give(cakes, finish, x, y)
                if debug:
                    print_cakes(cakes, finish)

    print "Case #{}:".format(i)
    print_cakes(cakes, finish)


