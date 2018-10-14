#Name: Robin Park
#Username: robinp
#Google Code Jam Round 1B 2017

import random
import math

possible = False

def adj(x, y):
    if x[0] == 'R':
        if y[0] == 'O' or y[0] == 'V' or y[0] == 'R':
            return False
    if x[0] == 'O':
        if y[0] == 'O' or y[0] == 'Y' or y[0] == 'R':
            return False
    if x[0] == 'Y':
        if y[0] == 'O' or y[0] == 'Y' or y[0] == 'G':
            return False
    if x[0] == 'G':
        if y[0] == 'G' or y[0] == 'Y' or y[0] == 'B':
            return False
    if x[0] == 'B':
        if y[0] == 'G' or y[0] == 'V' or y[0] == 'B':
            return False
    if x[0] == 'V':
        if y[0] == 'B' or y[0] == 'V' or y[0] == 'R':
            return False

    return True


def recur(color):
    if possible == True:
        return
    if color == "R":
        R -= 1
    if color == "O":
        O -= 1
    if color == "Y":
        Y -= 1
    if color == "G":
        G -= 1
    if color == "B":
        B -= 1
    if color == "V":
        V -= 1

    count += 1
    answer += color

    if count == N:
        if adj(color, "R") and adj(color, answer):
            w.write(answer)
            possible = True
            return
        if adj(color, "O") and adj(color, answer):
            w.write(answer)
            possible = True
            return
        if adj(color, "Y") and adj(color, answer):
            w.write(answer)
            possible = True
            return
        if adj(color, "G") and adj(color, answer):
            w.write(answer)
            possible = True
            return
        if adj(color, "B") and adj(color, answer):
            w.write(answer)
            possible = True
            return
        if adj(color, "V") and adj(color, answer):
            w.write(answer)
            possible = True
            return
    if adj(color, "R") and R > 0:
        recur("R")
    if adj(color, "O") and O > 0:
        recur("O")
    if adj(color, "Y") and Y > 0:
        recur("Y")
    if adj(color, "G") and G > 0:
        recur("G")
    if adj(color, "B") and B > 0:
        recur("B")
    if adj(color, "V") and V > 0:
        recur("V")

    answer = answer[0:len(answer)-1]
    count -= 1

    if color == "R":
        R += 1
    if color == "O":
        O += 1
    if color == "Y":
        Y += 1
    if color == "G":
        G += 1
    if color == "B":
        B += 1
    if color == "V":
        V += 1
        
    

def solve(N, R, O, Y, G, B, V):

    #possible = False
    answer = ""
    count = 0

    if R > 0:
        recur("R")
    elif O > 0:
        recur("O")
    elif Y > 0:
        recur("Y")
    elif G > 0:
        recur("G")
    elif B > 0:
        recur("B")
    elif V > 0:
        recur("V")
    else:
        answer = "IMPOSSIBLE"


    if possible == False:
        answer = "IMPOSSIBLE"

    w.write('Case #' + str(t+1) + ': ')
    w.write(str(answer))
    w.write('\n')

            

if __name__ == '__main__':
    with open('unicorn.in', 'r') as file, open('unicorn.out', 'w') as w:  
        T = int(file.readline().strip())
        for t in range(T):
        
            N, R, O, Y, G, B, V = map(int, file.readline().strip().split())
            possible = False

            solve(N, R, O, Y, G, B, V)

print("done")
