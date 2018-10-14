input_file = open("d_small_input.txt", "r")
output_file = open("d_small_output.txt", "w")
T = int(input_file.readline())
for t in range(1, T+1):

    # Step 0: get started
    N, M = [int(x) for x in input_file.readline().split()]
    moves = [] #A list of tuples, showing what moves have been made so far.
    the_floor = [["." for i in range(N)] for j in range(N)]

    # Step 1: place what we've been given
    for i in range(M):
        symbol, r, c = [x for x in input_file.readline().split()]
        the_floor[int(r) - 1][int(c) - 1] = symbol

    # Step 2: place the o
    if "x" in the_floor[0]:
        place = the_floor[0].index("x")
        the_floor[0][place] = "o"
        #Record this move
        moves.append((1, place + 1, "o"))
    elif "o" not in the_floor[0]:
        moves.append((1, 1, "o"))
        the_floor[0][0] = "o"
    if N > 1: #None of this should be done on the trivial case
        # Step 3: Fill the rest of the top row
        for i in range(N):
            if the_floor[0][i] == ".":
                the_floor[0][i] = "+"
                moves.append((1, i + 1, "+"))

        # Step 4: Place some +'s in the bottom row
        for i in range(1, N-1):
            the_floor[N-1][i] = "+"
            moves.append((N, i+1, "+"))

        # Step 5: Place the x's.
        if the_floor[0][0] is "o":
            #Place the x's diagonally downwards, starting from the 2nd row/column.
            for i in range(1, N):
                moves.append((i+1, i+1, "x"))
                the_floor[i][i] = "x"
        elif the_floor[0][N-1] is "o":
            for i in range(N-1):
                the_floor[N - i - 1][i] = "x"
                moves.append((N - i, i + 1, "x"))
        else:
            current_column = 0
            current_row = 1
            for i in range(N):
                if the_floor[0][current_column] is "o":
                    current_column += 1
                    continue
                the_floor[current_row][current_column] = "x"
                moves.append((current_row + 1, current_column + 1, "x"))
                current_column += 1
                current_row += 1

    calculated_points = 0
    for i in range(N):
        for j in range(N):
            if the_floor[i][j] == "x" or the_floor[i][j] == "+":
                calculated_points += 1
            elif the_floor[i][j] == "o":
                calculated_points += 2

    points = max(3 * N - 2, 2)

    if calculated_points != points:
        print("Got {}, expected {}".format(calculated_points, points))
    # Record stuff in the output file
    output_file.write("Case #{}: {} {}\n".format(t, points, len(moves)))
    for move in moves:
        output_file.write("{} {} {}\n".format(move[2], move[0], move[1]))

    #for row in the_floor:
    #    print(row)
    #print("=====")


#output_file.write("Case #{}: {}\n".format(t, tidy))
input_file.close()
output_file.close()
print("Files closed")
