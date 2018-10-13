#!c:\Python33\python.exe
# vim:fileencoding=utf-8

import sys
import re
import glob
import itertools
import pdb


def in_out():
    infiles = glob.glob("*.in")
    for infile in infiles:
        keyword = (sys.argv[1] if len(sys.argv)>1 else "test")
        if re.search(keyword, infile):
            return (open(infile,"r"), open(infile[:-2]+"out", "w+"))

def whowin(b, d):
    dddd=d*4
    for i in range(4):
        if b[0][i]+b[1][i]+b[2][i]+b[3][i]==dddd \
           or \
           b[i][0]+b[i][1]+b[i][2]+b[i][3]==dddd \
           or \
           b[0][0]+b[1][1]+b[2][2]+b[3][3]==dddd \
           or \
           b[0][3]+b[1][2]+b[2][1]+b[3][0]==dddd:
               return True
    return False




def main():
    fin,fout = in_out()
    casenum = int(fin.readline()[:-1])
    for k in range(casenum):
        l0 = list(fin.readline()[:-1])
        l1 = list(fin.readline()[:-1])
        l2 = list(fin.readline()[:-1])
        l3 = list(fin.readline()[:-1])
        board = [l0,l1,l2,l3]
        T=(4,4)
        Xwin=False
        Owin=False
        draw=True
        for i in range(4):
            for j in range(4):
                if board[i][j]=='T':
                    T=(i,j)
                if board[i][j]=='.':
                    draw=False
        if not T==(4,4):
            board[T[0]][T[1]]='X'
        Xwin = whowin(board, 'X')
        if not Xwin:
            if not T==(4,4):
                board[T[0]][T[1]]='O'
            Owin = whowin(board, 'O')

        fout.write('Case #'+str(k+1)+": ")
        if Xwin:
            fout.write("X won\n")
        elif Owin:
            fout.write("O won\n")
        elif draw:
            fout.write("Draw\n")
        else:
            fout.write("Game has not completed\n")
        tmp=fin.readline()

    fout.flush()
    fout.seek(0)
    print(fout.read())

if __name__ == "__main__":
    main()

