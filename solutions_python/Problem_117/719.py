def main():
    fileName = "B-large.in"
    file = open(fileName)

    # Loop for the number of tests there are.
    for case in range(1, int(file.readline())+1):
        # Read in the size of the board.
        line = file.readline().split()
        n = int(line[0])
        m = int(line[1])

        # Read in the board.
        board = []
        for _ in range(n):
            line = file.readline().split()
            board.append([int(char) for char in line])

        # Create a board to validate each grass.
        checkBoard = []
        for i in range(n):
            checkBoard.append([])
            for _ in range(m):
                checkBoard[i].append(".")

        canWork = True
        # Check every row.
        for i in range(n):
            # Find the larger edge.
            maxEdge = board[i][0]
            for j in range(1, m):
                if board[i][j] > maxEdge:
                    maxEdge = board[i][j]

            # Compare the row to this number.
            if canWork == True:
                for j in range(m):
                    if board[i][j] == maxEdge:
                        checkBoard[i][j] = "r"

        # Check every column.
        if canWork == True:
            for j in range(m):
                # Find the larger edge.
                maxEdge = board[0][j]
                for i in range(1, n):
                    if board[i][j] > maxEdge:
                        maxEdge = board[i][j]

                # Compare the col to this number.
                if canWork == True:
                    for i in range(n):
                        if board[i][j] == maxEdge:
                            checkBoard[i][j] = "c"

        # Check that the lower numbers came from somewhere.
        if canWork == True:
            for i in range(n):
                if canWork == True:
                    for j in range(m):
                        if checkBoard[i][j] == ".":
                            canWork = False
                            break

        # Print the solution.
        if canWork:
            print("Case #" + str(case) + ": YES")
        else:
            print("Case #" + str(case) + ": NO")

if __name__ == "__main__":
    main()

