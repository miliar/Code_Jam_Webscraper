import sys, math

def lin(n, p):
    return "." not in n and p not in n

def col(game, n, p):
    col = [game[0][n], game[1][n], game[2][n], game[3][n]]
    return "." not in col and p not in col

def diag1(game, p):
    diag = [game[0][0], game[1][1], game[2][2], game[3][3]]
    return "." not in diag and p not in diag 

def diag2(game, p):
    diag = [game[0][3], game[1][2], game[2][1], game[3][0]]
    return "." not in diag and p not in diag 
    
def calc(game):
    ongoing = False
    for i in range(len(game)):
        ongoing = ongoing or ("." in game[i])
        if lin(game[i], "O") or col(game, i, "O"):
            return "X won"
        if lin(game[i], "X") or col(game, i, "X"):
            return "O won"
            
    if diag1(game, "O") or diag1(game, "O"):
        return "X won"
    if diag1(game, "X") or diag2(game, "X"):
        return "O won"
    if ongoing:
        return "Game has not completed"
    return "Draw"
    
def main():
    f = open(sys.argv[1])
    for i in range(1, int(f.readline()) + 1):
        n = [f.readline(), f.readline(), f.readline(), f.readline()] 
        print "Case #" + str(i) + ":", calc(n)
        f.readline()
    f.close()
    
if __name__=="__main__":
    main()

