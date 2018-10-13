import fileinput

def read_file(File):
    text = File.read()
    lines = text.split('\n')
    return lines

lines = read_file(open('input.txt','r'));
n = int(lines[0]) #number of test cases


for i in range(n):
    line1 = lines[i*5 + 1]
    line2 = lines[i*5 + 2]
    line3 = lines[i*5 + 3]
    line4 = lines[i*5 + 4]
    completed = False
    
    for row in range(4):
        if ((lines[i*5 + row + 1][0]!='.') and (lines[i*5 + row + 1][1]==lines[i*5 + row + 1][0] or lines[i*5 + row + 1][1]=='T') and (lines[i*5 + row + 1][2]==lines[i*5 + row + 1][0] or lines[i*5 + row + 1][2]=='T') and (lines[i*5 + row + 1][3]==lines[i*5 + row + 1][0] or lines[i*5 + row + 1][3]=='T')):
            print('Case #'+str(i+1) + ': '+ lines[i*5 + row + 1][0]+' won')
            completed = True
            break
    if (completed == False):
        for col in range(4):
            if ((lines[i*5+1][col]!='.') and (lines[i*5+2][col]==lines[i*5+1][col] or lines[i*5+2][col]=='T') and (lines[i*5+3][col]==lines[i*5+1][col] or lines[i*5+3][col]=='T') and (lines[i*5+4][col]==lines[i*5+1][col] or lines[i*5+4][col]=='T')):#down
                print('Case #'+str(i+1) + ': '+ lines[i*5+1][col]+' won')
                completed = True
                break

    ##check diagonals
    if (completed == False):
        if (lines[i*5 + 1][0]!='.' and (line2[1]==line1[0] or line2[1]=='T') and (line3[2]==line1[0] or line3[2]=='T') and (line4[3]==line1[0] or line4[3]=='T')):
            print('Case #'+str(i+1) + ': '+ lines[i*5 + 1][0]+' won')
            completed = True
    if (completed == False):
        if (lines[i*5 + 1][3]!='.' and (line2[2]==line1[3] or line2[2]=='T') and (line3[1]==line1[3] or line3[1]=='T') and (line4[0]==line1[3] or line4[0]=='T')):
           print('Case #'+str(i+1) + ': '+ lines[i*5 + 1][3]+' won')
           completed = True

    if (completed == False):
        board = [line1,line2,line3,line4]
        draw = True
        for a in range(4):
            if (draw == False):
                break
            for b in range(4):
                if board[a][b] == '.':
                    print('Case #'+str(i+1) + ': Game has not completed')
                    draw = False
                    break
        if (draw):
            print('Case #'+str(i+1) + ': Draw')
            

