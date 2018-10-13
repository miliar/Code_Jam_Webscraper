t = int(input())

def flood_right(cake, row, col, char, col_mode):
    if row == len(cake) or col == len(cake[0]):
        return cake
    if cake[row][col] == '?':
        cake[row][col] = char
        if col_mode:
            return flood_right(cake, row + 1, col, char, col_mode)
        else:
            return flood_right(cake, row, col + 1, char, col_mode)
    else:
        return cake

def flood_left(cake, row, col, char, col_mode):
    # print(row,col)
    if row < 0 or col < 0:
        # print("returning", row,col)
        return cake
    if cake[row][col] == '?':
        cake[row][col] = char
        if col_mode:
            # print("flooding col up")
            return flood_left(cake, row - 1, col, char, col_mode)
        else:
            # print("flooding row left")
            return flood_left(cake, row, col - 1, char, col_mode)
    else:
        # print("done")
        return cake


for case in range(t):
    row, col = map(int,input().split())
    cake =[]
    cols = False


    for line in range(row):
        new_row = list(input())
        cake.append(new_row)
        if set(new_row) == set(['?']):
            cols = True

    # print("Begin filling cake in " + ("col" if cols else "row") + " mode")
    for r in range(row):
        for c in range(col):
            if cake[r][c] != '?':
                if cols:
                    # print("flooding col", c, "from", r)
                    cake = flood_left(cake, r-1, c, cake[r][c], cols)
                    # print("after up flood", cake)
                    cake = flood_right(cake, r+1, c, cake[r][c], cols)
                    # print("after down flood",  cake)
                else:
                    # print("flooding row", r, "from", c)
                    cake = flood_left(cake, r, c-1, cake[r][c], cols)
                    # print("after left flood", cake)
                    cake = flood_right(cake, r, c+1, cake[r][c], cols)
                    # print("after right flood",  cake)
    finished = True
    # print("Case #{}:".format(case+1))
    for line in cake:
        if "?" in line:
            finished = False
            break

    if not finished: #do it again?
        cols = False


        for line in range(row):
            if set(cake[line]) == set(['?']):
                cols = True

        # print("Begin filling cake in " + ("col" if cols else "row") + " mode")
        for r in range(row):
            for c in range(col):
                if cake[r][c] != '?':
                    if cols:
                        # print("flooding col", c, "from", r)
                        cake = flood_left(cake, r-1, c, cake[r][c], cols)
                        # print("after up flood", cake)
                        cake = flood_right(cake, r+1, c, cake[r][c], cols)
                        # print("after down flood",  cake)
                    else:
                        # print("flooding row", r, "from", c)
                        cake = flood_left(cake, r, c-1, cake[r][c], cols)
                        # print("after left flood", cake)
                        cake = flood_right(cake, r, c+1, cake[r][c], cols)
                        # print("after right flood",  cake)

    print("Case #{}:".format(case+1))
    for line in cake:
        print ("".join(line))
