'''
Created on Apr 13, 2013

@author: JuanTejada
'''
def main():
    lines = open("../../../input/codejam/A-large.in").read().splitlines()
    out = open('../../../output/ttt-large.txt', 'w+')
    cases = int(lines[0])
    il = 1
    
    for i in range(1,cases+1):
        complete = True
        board = []
        for j in range(il,il+4):
            if '.' in lines[j]:
                complete = False
            board.append(lines[j])
        il += 5
        
        won = False
        winnerLine = ''
        for j in range(len(board)):
            if wins(board[j]):
                winnerLine = board[j]
                won = True
                break
            elif wins([board[k][j] for k in range(len(board))]):
                winnerLine = [board[k][j] for k in range(len(board))]
                won = True
                break
                
        if not won:
            if wins([board[k][k] for k in range(len(board))]):
                winnerLine = [board[k][k] for k in range(len(board))]
                won = True
            elif wins([board[k][-(k+1)] for k in range(len(board))]):
                winnerLine = [board[k][-(k+1)] for k in range(len(board))]
                won = True
                
        case = "Case #"+str(i)+": "
        if won:
            if 'X' in winnerLine:
                out.write(case + "X won"+"\n")
            elif 'O' in winnerLine:
                out.write(case + "O won"+"\n")
        else:
            if complete:
                out.write(case + "Draw"+"\n")
            else:
                out.write(case + "Game has not completed"+"\n")
            
def wins(line):
    if line.count("X") == 4 or line.count("O") == 4 or (line.count("X") == 3 and line.count("T") == 1) or (line.count("O") == 3 and line.count("T") == 1):
        return True
    else:
        return False

if __name__ == "__main__":
    main()  

            