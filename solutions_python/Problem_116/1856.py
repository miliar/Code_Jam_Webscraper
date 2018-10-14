def main():
    fin = open("A-large.in", "rt")

    count = int(fin.readline())
    output = ""

    for x in range(count):
        board = ""

        # convert board to 1D array (string)
        for y in range(4):
            board += fin.readline().strip("\n")

        # clear the empty line
        fin.readline()

        winner = "Draw"

        results = [checkVert(board), checkHori(board), checkDiag(board)]
        gameOver = False

        for intrim in results:
            
            if True in intrim.keys():
                winner = str.format("{0} won", intrim[True])
                gameOver = True
                
            elif intrim["."] > 0:
                winner = "Game has not completed"

            if gameOver:
                break
        
        output += str.format("Case #{0}: {1}\n", x+1, winner)


    fin.close()

    fout = open("A-large.out", "wt")
    fout.write(output)
    fout.close()


def checkVert(board):
    out = dict()

    out[False] = ""
    out["."] = 0

    check = {0:"", 1:"", 2:"", 3:""} 
    
    for i in range(len(board)):
        
        if not board[i] == "T":
            
            if board[i] == ".":
                out["."] += 1
            
            if check[i%4] == "":
                check[i%4] = board[i]
                
            else:
                if not check[i%4] == board[i]:
                    check[i%4] = "N"

    for val in check.values():
        if val == "X" or val == "O":
            out[True] = val
        
    return out


def checkHori(board):
    out = dict()

    out[False] = ""
    out["."] = 0

    check = {0:"", 1:"", 2:"", 3:""} 
    
    for i in range(0,len(board),4):

        for j in range(4):
            if not board[i+j] == "T":
                
                if board[i+j] == ".":
                    out["."] += 1
                    
                if check[i/4] == "":
                    check[i/4] = board[i+j]
                    
                else:
                    if not check[i/4] == board[i+j]:
                        check[i/4] = "N"

                

    for val in check.values():
        if val == "X" or val == "O":
            out[True] = val
        
    return out


def checkDiag(board):
    longIndex = 5
    shortIndex = 3
    out = dict()

    out[False] = ""
    out["."] = 0

    check = {"long":"", "short":""} 
    
    for i in range(0,16,longIndex):
        
        if not board[i] == "T":
                        
            if board[i] == ".":
                out["."] += 1
                
            if check["long"] == "":
                check["long"] = board[i]
                
            else:
                if not check["long"] == board[i]:
                    check["long"] = "N"
                    
    for i in range(3,13,shortIndex):
        
        if not board[i] == "T":
                        
            if board[i] == ".":
                out["."] += 1
                
            if check["short"] == "":
                check["short"] = board[i]
                
            else:
                if not check["short"] == board[i]:
                    check["short"] = "N"
                    
    for val in check.values():
        if val == "X" or val == "O":
            out[True] = val
        
    return out

main()
