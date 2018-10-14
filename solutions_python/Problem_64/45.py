import sys                       
import os

def main():
    s = ''.join(sys.stdin.readlines()).split()
    os.close(0)

    T = int(s[0])
    s = s[1:]

    for i in range(T):
        M = int(s[0])
        N = int(s[1])
        s = s[2:]
        board = []
        for j in range(M):
            dec = int(s[0],16)
            s = s[1:]
            bin = ''
            log = N
            while log > 0:
                bin = str(dec%2) + bin
                dec = dec / 2
                log -= 1
            board += [list(bin)]
        dict = {}
        while True:
            #prettyPrint(board)
            large = findLarge(board)
            if large[1] == 0:
                break
            if dict.has_key(large[1]):
                dict[large[1]] += 1
            else:
                dict[large[1]] = 1
            board = fill(board,large)
        sizes = dict.keys()
        sizes.sort()
        sizes.reverse()
        print "Case #" + str(i+1) + ": " + str(len(sizes))
        for size in sizes:
            print str(size) + " " + str(dict[size])

def fill(board,large):
    for i in range(large[0][0], large[0][0] + large[1]):
        for j in range(large[0][1], large[0][1] + large[1]):
            board[i][j] = False
    return board

def findLarge(board):
    largePos = (-1,-1)
    largeSize = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            size = findSquare(board, i, j)
            if size > largeSize:
                largeSize = size
                largePos = (i,j)
    return (largePos,largeSize)

def findSquare(board,row,col):
    if not board[row][col]:
        return 0
    size = 1
    mod = 1
    while True:
        if not (row < len(board)-mod and col < len(board[0])-mod):
            return mod
        for i in range(mod+1):
            if not (board[row+i][col+mod] and board[row+i][col+mod] != board[row+i][col+mod-1]):
                return mod
            if not (board[row+mod][col+i] and board[row+mod][col+i] != board[row+mod-1][col+i]):
                return mod
        mod += 1

def prettyPrint(board):
    for i in range(len(board)):
        out = ""
        for j in range(len(board[0])):
            if not board[i][j]:
                out += "F "
            else:
                out += board[i][j] + " "
        print out[:-1]


        


if __name__ == "__main__":
 	main()

