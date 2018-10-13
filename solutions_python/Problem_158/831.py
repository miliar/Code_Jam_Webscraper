# ProblemC GCJ 2015
import math
f = open("input.in", "r")
fout = open("output.out", "w")
tot = f.readlines()

T = int(tot[0])

for i in range(1,T+1):
    ok = False
    line = tot[i].strip().split(" ")
    X = int(line[0])
    R = int(line[1])
    C = int(line[2])
    if(X==1):
        ok = True
    elif(X==2 and R*C%2==0):
        ok = True # gabriel
    elif(X==2): #and R*C%2!=0):
        ok = False #richard

        
    elif(X==3 and R*C%3!=0):
        ok = False
    elif(X==3 and (R==1 or C==1)):
        ok = False
    elif(X==3 and R*C%3==0 and R>=2 and C>=2):
        ok = True

    elif(X==4 and R*C%4!=0):
        ok=False
    elif(X==4 and R>=3 and C>=3): #e ovviamente rc = 0 mod 4
        ok = True
    if ok:
        s="GABRIEL"
    else:
        s="RICHARD"
    fout.write("Case #{0}: {1}\n".format(i,s))
fout.close()
