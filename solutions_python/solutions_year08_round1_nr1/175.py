import math
import copy

f=open('A-large.in')
out = open('vectorout.txt','w')
casemax = int(f.readline())
for i in range (casemax):
    n = int(f.readline())
    StrXtemp = f.readline()
    StrYtemp = f.readline()
    StrX = StrXtemp.split()
    StrY = StrYtemp.split()
    VecX = []
    VecY = []
    for j in range (n):
        VecX.append (int(StrX[j]))
        VecY.append (int(StrY[j]))
    VecX.sort()
    VecY.sort()
    prod = 0
    for j in range (n):
        prod = prod + VecX[j]*VecY[n-j-1]
    print i
    out.write('Case #'+str(i+1)+": "+str(prod)+"\n")
    
