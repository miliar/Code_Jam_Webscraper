#-------------------------------------------------------------------------------
# Name:        Tic-Tac-Toe-Tomek
# Purpose:
#
# Author:      udonko
#
# Created:     14/04/2013
# Copyright:   (c) udonko 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import sys
class Resolve:
    def __init__(self, board):
        self.board = []
        self.board = board
    def checkcell(self, x,y,char):
        if self.board[x][y] == char or self.board[x][y] == "T":
            return True
        else:
            return False

    def check(self, char, pattern):

        for pos in pattern:
            result = self.checkcell(pos[0],pos[1], char)
            if result == False:
                return False
        return True
    def resolve(self):
        patterns = [
            [(0,0),(0,1),(0,2),(0,3)],
            [(1,0),(1,1),(1,2),(1,3)],
            [(2,0),(2,1),(2,2),(2,3)],
            [(3,0),(3,1),(3,2),(3,3)],
            [(0,0),(1,0),(2,0),(3,0)],
            [(0,1),(1,1),(2,1),(3,1)],
            [(0,2),(1,2),(2,2),(3,2)],
            [(0,3),(1,3),(2,3),(3,3)],

            [(0,0),(1,1),(2,2),(3,3)],
            [(3,0),(2,1),(1,2),(0,3)],
            ]
        for char in ["X","O"]:
            for pattern in patterns:
                result = self.check(char, pattern)
                if result == True:
                    return char + " won"

        dotExist = False
        for i in range(4):
            if "." in self.board[i]:
                dotExist = True
                break
        if dotExist == True:
            return "Game has not completed"
        else:
            return "Draw"
def main():
    infile = open("input.txt","r")
    outfile = open("output.txt","w")
    num = int(infile.readline())
    board = ["" for i in range(4)]
    # num of test loop
    for i in range(num):

        for j in range(4):
            board[j] = infile.readline()

        #resolve
        resolve = Resolve(board)
        ret = resolve.resolve()
        outfile.write("Case #"+str(i+1)+": "+ret+"\n")

        infile.readline()

    infile.close()
    outfile.close()

if __name__ == '__main__':
    main()
