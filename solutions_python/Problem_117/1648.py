#Code Jam 2013 - QR - PB
#Ben Fishbein
#4/13
#Lawnmower
#See if a lawn can be mowed in a certain style
#https://code.google.com/codejam/contest/2270488/dashboard#s=p1

into = open('CJ2013QRPB1.in')
out = open('CJ2013QRPB1.out', 'w')
#into = open('CJ2013QRPB2.in')
#out = open('CJ2013QRPB2.out', 'w')

lines = []
lines = into.readlines()
lineCount = 1

board = []
board2 = []
row = []
row2 = []
can = 1

for x in range(int(lines[0])):
    boardParams = lines[lineCount].split()
    lineCount = lineCount + 1
    for i in range(int(boardParams[0])):
        #print lineCount
        row = lines[lineCount].split()
        lineCount = lineCount + 1
        board.append(row)
    for i in board[0]:
        board2.append([])
    #print board2
    #print board
    for i in range(len(board)):
        for j in range(len(board[i])):
          #  print j, len(board[i])
            board2[j].append(board[i][j])
        row2 = []
   # print board, "GERAWEGRA"
  #  print board2, "AGSAFEA"
    for i in range(int(boardParams[0])):
        for j in range(int(boardParams[1])):
         #   print int(board[i][j])
        #    print int(board2[j][i])
            if (int(board[i][j]) >= int(max(board[i])) or  int(board2[j][i]) >= int(max(board2[j]))):
                True
            else:
                can = 0
             #   print board[i][j], "abdfbf"
   # print board
    #print board2
    board = []
    board2 = []
        
    if (can == 1):
        out.write("Case #" + str(x + 1) + ": " + "YES\n")
        print "YES"
    else:
        out.write("Case #" + str(x + 1) + ": " + "NO\n")
        print "NO"
    can = 1
out.close()
