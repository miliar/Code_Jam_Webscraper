#Tested locally with Python 2.6.2 on OS X 10.6.3
import math

input = open('A-large.in','r')
output = open('A-large.out','w')
T = int(input.next())

for i in range(0,T):
    N = int(input.next())
    A = []
    B = []
    for j in range(0,N):
        numsin = input.next().split(' ')
        A.append(int(numsin[0]))
        B.append(int(numsin[1]))
   
    count = 0
    for j in range(0,N):
        for k in range(j+1,N):
             if((A[j]-A[k])*(B[j]-B[k]) < 0):
                 count+=1

    output.write("Case #"+str(i+1)+": "+str(count)+"\n")
