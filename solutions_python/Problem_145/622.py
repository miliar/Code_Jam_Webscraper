input = open("a.in" , "r")
output = open("a.out" , "w")

from math import ceil, log
from fractions import Fraction

T = int(input.readline())

for i in range(1, T + 1):
    P, Q = map(int, input.readline().split("/"))
    P, Q = map(int, str(Fraction(P, Q)).split("/"))
    c = 0
    b = log(Q)/log(2)
    if int(b) != b:
        c = "impossible"
    else:
        x = int(log(P)/log(2))
        c = str(int(b - x))
    print c
    output.write("Case #" + str(i) + ": " + str(c) + "\n")    
input.close()
output.close()
