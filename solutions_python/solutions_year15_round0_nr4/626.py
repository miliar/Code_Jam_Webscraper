#!/usr/bin/python

import math

def ominous_omino(X, R, C):
    total = R * C
    number_of_Xs = total / X
    possible = not (math.modf(number_of_Xs)[0])
    if possible:
        smallest = min(R, C)
        if X>2 and smallest==1:
            possible = False
        if X==4 and smallest==2:
            possible = False
    return "GABRIEL" if possible else "RICHARD"
    
def main():
    with open('input.in', 'r') as f:
        with open('output.txt', 'w') as o:
            n = int(f.readline().rstrip('\n'))
            for i in range(n):
                X, R, C = list(map(int, f.readline().rstrip('\n').split(' ')))
                result = "Case #" + str(i + 1) + ": " + ominous_omino(X, R, C)
                print(result)
                o.write(result + "\n")

if __name__=="__main__":
    main()
