def main():
    fileName = "A-large.in"
    file = open(fileName)
    
    # Loop for the number of tests there are.
    numCases = int(file.readline())
    for case in range(1, numCases+1):
        # Read in the board.
        board = []
        for _ in range(4):
            line = [char for char in file.readline()]
            board.append(line)

        determinedWinner = False
        # If the whole row is the same.
        for i in range(4):
            char = board[i][0]
            for j in range(1, 4):
                if char != ".":
                    if char != "T":
                        tempChar = board[i][j]
                        if tempChar != char and tempChar != "T":
                            break
                    else:
                        char = board[i][j]
                else:
                    break
            else:        
                print("Case #" + str(case) + ": " + char + " won")
                determinedWinner = True
                break

        # If the whole col is the same.
        if determinedWinner == False:
            for j in range(4):
                char = board[0][j]    
                for i in range(1, 4):
                    if char != ".":
                        if char != "T":
                            tempChar = board[i][j]
                            if tempChar != char and tempChar != "T":
                                break
                        else:
                            char = board[i][j]
                    else:
                        break
                else:        
                    print("Case #" + str(case) + ": " + char + " won")
                    determinedWinner = True
                    break

        # If the negative diagonal is the same.
        if determinedWinner == False:
            char = board[0][0]
            for x in range(1, 4):
                if char != ".":
                    if char != "T":
                        tempChar = board[x][x]
                        if tempChar != char and tempChar != "T":
                            break
                    else:
                        char = board[x][x]
                else:
                    break
            else:
                print("Case #" + str(case) + ": " + char + " won")
                determinedWinner = True

        # If the positive diagonal is the same.
        if determinedWinner == False:
            char = board[0][3]
            for x in range(1, 4):
                if char != ".":
                    if char != "T":
                        tempChar = board[x][3-x]
                        if tempChar != char and tempChar != "T":
                            break
                    else:
                        char = board[x][3-x]
                else:
                    break
            else:
                print("Case #" + str(case) + ": " + char + " won")
                determinedWinner = True

        # If the whole board is filled.
        boardFilled = True;
        if determinedWinner == False:
            for i in range(4):
                if boardFilled == True:
                    for j in range(4):
                        if board[i][j] == ".":
                            boardFilled = False
                            break

        if determinedWinner == False and boardFilled == True:
            print("Case #" + str(case) + ": Draw")

        # Else the game has not been completed yet.
        if determinedWinner == False and boardFilled == False:
            print("Case #" + str(case) + ": Game has not completed")

        # Read in the empty line.
        if case != numCases:
            line = file.readline()

if __name__ == "__main__":
    main()

