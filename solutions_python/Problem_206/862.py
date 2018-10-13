from decimal import *

fout = open("A-large.out", "w")
f = open("A-large.in","r")
L = f.readlines()
i = 1

for test_case in range(int(L[0])):
    D, N = map(int,L[i].split(" "))
    D= Decimal(D)
    tMin = Decimal(-1.0)
    for n in range(N):
        i+=1
        K, S = map(int,L[i].split(" "))
        K = Decimal(K)
        S = Decimal(S)
        T = (D - K)/S
        tMin = max(T, tMin)
    fout.write("Case #")
    fout.write(str(test_case+1))
    fout.write(": ")
    fout.write(str(D/tMin)) 
    fout.write("\n")
    i+=1