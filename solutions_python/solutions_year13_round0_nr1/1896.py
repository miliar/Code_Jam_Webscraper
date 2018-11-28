myfile = open("A-large.in.txt", "r")
output = open("output.txt", "w")

cases = int(myfile.readline())
win = ["XXXX", "XTXX", "XXTX", "XXXT", "TXXX", "OOOO", "TOOO", "OTOO", "OOTO", "OOOT"]
for case in range(cases):
    result = ""
    tloc = ""
    board = []
    for x in range(4):
        board.append(myfile.readline().strip())
    dia1 = ""
    dia2 = ""
    row1 = ""
    row2 = ""
    row3 = ""
    row4 = ""
    for i in range(len(board)):
        dia1=dia1+board[i][i]
        dia2=dia2+board[i][3-i]
        row1=row1+board[i][0]
        row2=row2+board[i][1]
        row3=row3+board[i][2]
        row4=row4+board[i][3]
    test =[dia1, dia2, board[0], board[1], board[2], board[3], row1, row2, row3, row4]
    
    for item in test:
        if item in win:
            if "X" in item:
                result = "X won"
            elif "O" in item:
                result = "O won"
    if result == "":
        for row in board:
            if "." in row:
                result = "Game has not completed"
    if result == "":
        result = "Draw"
    out = "Case #%d: " %(case+1) +result
    output.write(out+"\n")
    myfile.readline()

myfile.close()
output.close()
