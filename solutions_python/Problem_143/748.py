import sys
import random

def rand(n):
    return random.randint(0,n)

file = open("problem.in")

for cases in range(int(file.readline())):
    (First,Second,K) = file.readline().split()
    win = 0
    for NumberFirst in range(int(First)):
        for NumberSecond in range(int(Second)):
            NewValue = NumberSecond & NumberFirst
            if(NewValue < int(K)):
                win+=1
    print("Case #" + str(cases+1) + ": " + str(win))
