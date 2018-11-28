cases = int(raw_input())
case = 1

def checkColumn(game, col, piece):
    
    return ((game[0][col] == piece or game[0][col] == "T") and 
            (game[1][col] == piece or game[1][col] == "T") and
            (game[2][col] == piece or game[2][col] == "T") and
            (game[3][col] == piece or game[3][col] == "T"))
           
def checkRow(game, row, piece):
    
    return ((game[row][0] == piece or game[row][0] == "T") and 
            (game[row][1] == piece or game[row][1] == "T") and
            (game[row][2] == piece or game[row][2] == "T") and
            (game[row][3] == piece or game[row][3] == "T"))
            
def checkDiagonal(game, piece):
    
    return (((game[0][0] == piece or game[0][0] == "T") and 
             (game[1][1] == piece or game[1][1] == "T") and
             (game[2][2] == piece or game[2][2] == "T") and
             (game[3][3] == piece or game[3][3] == "T")) or
            ((game[0][3] == piece or game[0][3] == "T") and 
             (game[1][2] == piece or game[1][2] == "T") and
             (game[2][1] == piece or game[2][1] == "T") and
             (game[3][0] == piece or game[3][0] == "T")))

while case <= cases:
    
    game = []
    game.append(raw_input().strip())
    game.append(raw_input().strip())
    game.append(raw_input().strip())
    game.append(raw_input().strip())
    done = False
    
    for piece in ["X", "O"]:
        for i in range(4):
            if not done and (checkRow(game, i, piece) or checkColumn(game, i, piece)):
                print "Case " + "#" + str(case) + ": " + piece + " won"
                done = True
                break
        if not done and checkDiagonal(game, piece):
            print "Case " + "#" + str(case) + ": " + piece + " won"
            done = True
        if done:
            break
    
    if not done:
        if "." not in game[0] + game[1] + game[2] + game[3]:
            done = True
            print "Case " + "#" + str(case) + ": Draw"
            
    if not done:
        print "Case " + "#" + str(case) + ": Game has not completed"
    
    raw_input()
    case += 1
