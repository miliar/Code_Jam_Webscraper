import random

def rand(n):
    return random.randint(0,n)

import sys
f = open("data2.txt")

for i in range(int(f.readline())):
    (A,B,K) = f.readline().split()
    wins = 0
    for nA in range(int(A)):
        for nB in range(int(B)):
            winner = nA & nB
            if(winner < int(K)):
                wins+=1
    print("Case #" + str(i+1) + ": " + str(wins))
