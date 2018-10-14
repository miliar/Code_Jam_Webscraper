from __future__ import print_function
import fileinput
import re

def main(loc=""):
    raw = input('input location: ')
    f = open(raw,'r+')
    o = open("C:/Users/Matt/Desktop/output.txt",'w')
    num = int(f.readline()) #num of inputs
    board=""
    inp=[]
    for j in xrange(0,num):
        board=""
        inp = readinput(f,4,1)
        for lines in inp:
            board+=lines
        for i in xrange(0,4): # check verticals + horizontals
            leave=False
            if (board[i] =='T' or board[i]=="X") and (board[i+4]=="T" or board[i+4]=="X") and (board[i+8]=="T" or board[i+8]=="X") and (board[i+12] == 'T' or board[i+12]=="X"):
                done(1,j,o)
            elif (board[i] =='T' or board[i]=="O") and (board[i+4]=="T" or board[i+4]=="O") and (board[i+8]=="T" or board[i+8]=="O") and (board[i+12] == 'T' or board[i+12]=="O"):
                done(2,j,o)
            elif (board[4*i] =='T' or board[4*i]=="X") and (board[4*i+1]=="T" or board[4*i+1]=="X") and (board[4*i+2]=="X" or board[4*i+2]=="X") and (board[4*i+3] == 'T' or board[4*i+3]=="X"):
                done(1,j,o)
            elif (board[4*i] =='T' or board[4*i]=="O") and (board[4*i+1]=="T" or board[4*i+1]=="O") and (board[4*i+2]=="T" or board[4*i+2]=="O") and (board[4*i+3] == 'T' or board[4*i+3]=="O"):
                done(2,j,o)
            else:
                continue
            leave = True
            break
        if leave == True:
            continue
        if (board[0]=="X" or board[0]=="T") and (board[5]=="X" or board[5]=="T") and (board[10]=="X" or board[10]=="T") and (board[15]=="X" or board[15]=="T"):
            done(1,j,o)
            continue
        elif (board[0]=="O" or board[0]=="T") and (board[5]=="O" or board[5]=="T") and (board[10]=="O" or board[10]=="T") and (board[15]=="O" or board[15]=="T"):
            done(2,j,o)
            continue
        
        if (board[3]=="X" or board[3]=="T") and (board[6]=="X" or board[6]=="T") and (board[9]=="X" or board[9]=="T") and (board[12]=="X" or board[12]=="T"):
            done(1,j,o)
            continue
        elif (board[3]=="O" or board[3]=="T") and (board[6]=="O" or board[6]=="T") and (board[9]=="O" or board[9]=="T") and (board[12]=="O" or board[12]=="T"):
            done(2,j,o)
            continue
    
        match =re.search(r'\.+', board)
        if match:
            done(4,j,o)
            continue
        else:
            done(3,j,o)
            continue
    

def done(end,num,filename):
    result=""
    if end == 1:
        result = "X won"
    elif end == 2:
        result = "O won"
    elif end== 3:
        result = "Draw"
    elif end== 4:
        result = "Game has not completed"
    filename.write('Case #'+str(num+1)+': '+result+'\n')
    #return num + 1
        

def readinput(filename,lines,trash=1): #read in filename x lines, trash y lines after
    inp=[]
    for i in xrange(0,lines):
        inp.append(filename.readline().replace('\n', ''))
    for j in xrange(0,trash):
        filename.readline()
    return inp

main()
