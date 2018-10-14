#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description="google code jam practice all your base")
parser.add_argument("inputfile", type=str, help="input file")
args = parser.parse_args()
outfile = open("output_tomek.out","w")

def read_input():
    f = open(args.inputfile)
    T = int(f.readline())
    for i in range(T):
        board = []
        for i in range(4):
            board.append(f.readline().strip())
        _ = f.readline()
        yield board


def output(n ,s):
    outstring = "Case #{}: {}\n".format(n+1, s)
    print(outstring, end="")
    outfile.write(outstring)

def find_K_consecutive(K, N, board):
    X_wins = O_wins = False
    for i in range(N):
        for j in range(N):
            piece = board[i][j]
            if piece not in "XOT":
                continue
            for a, b in [(a, b) for a in range(-1, 2) for b in range(-1, 2)]:
                if(a == b == 0):
                    continue
                for k in range(1, K):
                    x = i + k * a
                    y = j + k * b
                    if(x < 0 or x >= N or y < 0 or y >= N):
                        continue
                    # print(x,y)
                    # print(board)
                    if board[x][y] != piece and board[x][y] != "T":
                        break
                    if(k == K - 1):
                        if piece == "X":
                            X_wins = True
                        else:
                            O_wins = True
    return (X_wins, O_wins)

def draw(board):
    for line in board:
        if "." in line:
            return False
    return True

def main():
    for n,case in enumerate(read_input()):
        #print(case)
        X_wins, O_wins = find_K_consecutive(4, 4, case)
        if(X_wins):
            outstring = "X won"
        elif(O_wins):
            outstring = "O won"
        else:
            if(draw(case)):
                outstring = "Draw"
            else:
                outstring = "Game has not completed"
        output(n,outstring)

if __name__ == "__main__":
    main()
