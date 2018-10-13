from math import *
#File IO stuff
f = open("input.in", "r")
o = open("COutput.out", "w")

#Constants and stuff
T = eval(f.readline())
for i in range(T):
    count=0
    A, B = f.readline().strip("\n").split(" ")
    A, B = eval(A), eval(B)
    for j in range(A,B+1): # <=A and >=B
        if str(j)==str(j)[::-1]:
            noa = str(sqrt(j)).split(".")
            if noa[1]=="0" and str(trunc(sqrt(j)))==str(trunc(sqrt(j)))[::-1]:
                count+=1
    print("Case #{0}: {1}".format(i+1, count))
    o.write("Case #{0}: {1}\n".format(i+1, count))