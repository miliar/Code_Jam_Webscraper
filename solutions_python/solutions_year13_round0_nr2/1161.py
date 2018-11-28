#-------------------------------------------------------------------------------
# Name:        Lawnmower
# Purpose:
#
# Author:      udonko
#  python 2.7
# Created:     14/04/2013
# Copyright:   (c) udonko 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python]
import sys
class Resolve:
    def __init__(self, board, n, m):
        self.board = []
        self.board = board
        self.field = [[100 for i in range(m)] for j in range(n)]
        self.n = n
        self.m = m
    def isEqual(self):
        for i in range(n):
            for j in range(m):
                if self.field[n][m] !=self.board[n][m]:
                    return False
        return True
    def canContinue(self):
        for i in range(n):
            for j in range(m):
                if self.field[n][m] < self.board[n][m]:
                    return False
        return True
    def resolve(self):

        while(True):
            if self.isEqual() == True:
                return "YES"
            if self.canContinue() == False:
                return "NO"
    def resolve2(self):

        for i in range(self.n):
            for j in range(self.m):
                value = self.board[i][j]
                left = False
                right = False
                top = False
                bottom = False
                for x in range(self.n):
                    if x == i: continue
                    if self.board[x][j] > value :
                        if x < i:
                            left = True
                        if x > i:
                            right = True
                        break

                for x in range(self.m):
                    if x == j: continue
                    if self.board[i][x] > value :
                        if x < j:
                            top = True
                        if x > j:
                            bottom = True
                        break
                #sys.stdout.write("i="+str(i)+",j="+str(j)+"----\n")
                #sys.stdout.write(str(left)+","+str(right)+","+str(top)+","+str(bottom)+ "\n")
                if (top == True or bottom == True) and (left == True or right == True):
                    return "NO"
        return "YES"
def main():
    infile = open("input.txt","r")
    outfile = open("output.txt","w")
    num = int(infile.readline())
    board = ["" for i in range(4)]
    # num of test loop
    for i in range(num):
        #sys.stdout.write(str(i)+"----\n")
        temp = infile.readline()
        temps = temp.split()
        n = int(temps[0])
        m = int(temps[1])
        board = [[] for x in range(n)]
        for j in range(n):
            temp = infile.readline()
            temps = temp.split()
            board[j] = [int(val) for val in temps]


        #resolve
        resolve = Resolve(board,n,m)
        ret = resolve.resolve2()
        outfile.write("Case #"+str(i+1)+": "+ret+"\n")



    infile.close()
    outfile.close()

if __name__ == '__main__':
    main()
