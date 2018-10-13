import os
import math

def is_horizontally_preset(table,move):
    x0 = ord(table[0])+ord(table[1])+ord(table[2])+ord(table[3])
    x1 = ord(table[4])+ord(table[5])+ord(table[6])+ord(table[7])
    x2 = ord(table[8])+ord(table[9])+ord(table[10])+ord(table[11])
    x3 = ord(table[12])+ord(table[13])+ord(table[14])+ord(table[15])
    if( (x0 == 4*ord(move)) or (x0 == (3*ord(move)+ord('T')))):
        return True
    if( (x1 == 4*ord(move)) or (x1 == (3*ord(move)+ord('T')))):
        return True
    if( (x2 == 4*ord(move)) or (x2 == (3*ord(move)+ord('T')))):
        return True
    if( (x3 == 4*ord(move)) or (x3 == (3*ord(move)+ord('T')))):
        return True
    return False
    

    
def is_vertically_preset(table,move):
    x0 = ord(table[0])+ord(table[4])+ord(table[8])+ord(table[12])
    x1 = ord(table[1])+ord(table[5])+ord(table[9])+ord(table[13])
    x2 = ord(table[2])+ord(table[6])+ord(table[10])+ord(table[14])
    x3 = ord(table[3])+ord(table[7])+ord(table[11])+ord(table[15])
    if( (x0 == 4*ord(move)) or (x0 == (3*ord(move)+ord('T')))):
        return True
    if( (x1 == 4*ord(move)) or (x1 == (3*ord(move)+ord('T')))):
        return True
    if( (x2 == 4*ord(move)) or (x2 == (3*ord(move)+ord('T')))):
        return True
    if( (x3 == 4*ord(move)) or (x3 == (3*ord(move)+ord('T')))):
        return True
    return False

def is_diagonally_preset(table,move):
    x0 = ord(table[0])+ord(table[5])+ord(table[10])+ord(table[15])
    x1 = ord(table[3])+ord(table[6])+ord(table[9])+ord(table[12])
    if( (x0 == 4*ord(move)) or (x0 == (3*ord(move)+ord('T')))):
        return True
    if( (x1 == 4*ord(move)) or (x1 == (3*ord(move)+ord('T')))):
        return True
    return False
   
    
def main():
    f = open("A-large.in","r")
    doc = f.read().split('\n')   
    num_test_cases = int(doc[0])
    cum_idx  = 1
    for i in range(0, num_test_cases):
        table = ""
        for idx in range(0,4):
            table = table+doc[cum_idx+idx]
        cum_idx= cum_idx+5

        #print table+"\n\n"

        if (is_horizontally_preset(table,'X') is True) or (is_vertically_preset(table,'X') is True) or ( is_diagonally_preset(table,'X')is True):
            print "Case #"+str(i+1)+": "+ "X won"
            continue

        elif (is_horizontally_preset(table,'O') is True) or (is_vertically_preset(table,'O') is True) or ( is_diagonally_preset(table,'O')is True):
            print "Case #"+str(i+1)+": "+ "O won"
            continue

        elif table.__contains__('.'):
            print "Case #"+str(i+1)+": "+ "Game has not completed"        
    
        else:
            print "Case #"+str(i+1)+": "+ "Draw"
            

if __name__ == "__main__":
    main()

