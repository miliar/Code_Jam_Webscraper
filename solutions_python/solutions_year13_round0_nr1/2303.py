# -*- coding:Utf-8 -*-
import os
from getopt import getopt, GetoptError
from sys import argv

# Google Code Jam 2013
# Tic Tac Toe Tomek 
# coded by AiMeCee - Reunion

def main() :
    ls_X_win = ['XXXX','XXXT','XXTX','XTXX','TXXX']
    ls_O_win = ['OOOO','OOOT','OOTO','OTOO','TOOO']
    f_input=argv[1:][0]
    (base,ext)=os.path.splitext(f_input)
    f_output= base+"_solved"+ext
    read_input = open(f_input,'r')
    write_output = open(f_output,'w')
    line1 = read_input.readline()
    nb_cases = int(line1)
    for case in range (1,nb_cases+1) :
        game_l1 = read_input.readline()
        game_l2 = read_input.readline()
        game_l3 = read_input.readline()
        game_l4 = read_input.readline()
        game_l1, game_l2, game_l3, game_l4 = game_l1[:4], game_l2[:4], game_l3[:4], game_l4[:4]
        game_c1 = game_l1[0]+game_l2[0]+game_l3[0]+game_l4[0]
        game_c2 = game_l1[1]+game_l2[1]+game_l3[1]+game_l4[1]
        game_c3 = game_l1[2]+game_l2[2]+game_l3[2]+game_l4[2]
        game_c4 = game_l1[3]+game_l2[3]+game_l3[3]+game_l4[3]
        game_d1 = game_l1[0]+game_l2[1]+game_l3[2]+game_l4[3]
        game_d2 = game_l1[3]+game_l2[2]+game_l3[1]+game_l4[0]
        completed=True
        winner = ''
        if '.' in game_l1+game_l2+game_l3+game_l4 :
            completed = False
        for line in [game_l1,game_l2,game_l3,game_l4,game_c1,game_c2,game_c3,game_c4,game_d1,game_d2] :
            if line in ls_X_win :
                winner = 'X'
                break
            elif line in ls_O_win :
                winner = 'O'
                break
        if winner == 'X' :
            endmsg = 'X won\n'
        elif winner == 'O' :
            endmsg = 'O won\n'
        elif completed :
            endmsg = 'Draw\n'
        else :
            endmsg = 'Game has not completed\n'
        msg = 'Case #'+str(case)+": "+endmsg
        write_output.writelines(msg)
        separator_line= read_input.readline()
    read_input.close()
    write_output.close()
    
    
if __name__ == "__main__" :
    main()