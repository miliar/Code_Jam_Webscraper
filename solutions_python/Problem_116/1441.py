# -*- coding: utf-8 -*-

def func(line):
    global ret_words
    if line.count("X") == 4:
        return 0
    elif line.count("X") == 3 and line.count("T") == 1:
        return 0
    elif line.count("O") == 4:
        return 1
    elif line.count("O") == 3 and line.count("T") == 1:
        return 1
    elif line.count(".") == 0:
        return -110
    elif line.count("X") + line.count("O") + line.count("T") < 4:
        return -11
    else:
        return -10000
    

if __name__ == '__main__':
    f = open('A-large.in.txt')
    ofile = open('output.txt', 'w')
    N = f.readline()
    
    for case in range(int(N)):
        board = [[0 for j in range(4)] for i in range(4)]
        
        board[0] = f.readline()
        board[1] = f.readline()
        board[2] = f.readline()
        board[3] = f.readline()
        f.readline()
        
        i = 0
        xFlag = False
        oFlag = False

        # 横
        for row in range(4):
            ret = int(func(board[row]))
            if ret == 0:
                xFlag = True
            elif ret == 1:
                oFlag = True
            else:
                i = i + ret

        # 縦
        # 転地
        if i < 0:
            board2 = map(list, zip(*board))
            for row in range(4):
                ret = int(func(board2[row]))
                if ret == 0:
                    xFlag = True
                elif ret == 1:
                    oFlag = True
                else:
                    i = i + ret

        # 斜め
        if i < 0:
            skew = str(board[0][0]) + str(board[1][1]) + str(board[2][2]) + str(board[3][3])
            ret = int(func(skew))
            if ret == 0:
                xFlag = True
            elif ret == 1:
                oFlag = True
            else:
                i = i + ret

        if i < 0:
            skew = str(board[0][3]) + str(board[1][2]) + str(board[2][1]) + str(board[3][0])
            ret = int(func(skew))
            if ret == 0:
                xFlag = True
            elif ret == 1:
                oFlag = True
            else:
                i = i + ret
                
        if xFlag:
            print "Case #" + str(case + 1) + ": X won"
            ofile.write("Case #" + str(case + 1) + ": X won\n")
        elif oFlag:
            print "Case #" + str(case + 1) + ": O won"
            ofile.write("Case #" + str(case + 1) + ": O won\n")
        elif i == -1100:
            print "Case #" + str(case + 1) + ": Draw"
            ofile.write("Case #" + str(case + 1) + ": Draw\n")
        elif i < 0:
            print "Case #" + str(case + 1) + ": Game has not completed"
            ofile.write("Case #" + str(case + 1) + ": Game has not completed\n")
        
        
    f.close()
    
