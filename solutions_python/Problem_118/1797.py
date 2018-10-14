f=open("C-small.in","r")
g=open("pal.out","w")
import math
T = int(f.readline())

def pal(num):
    return str(num) == str(num)[::-1]

for i in range(0,T):
  X = f.readline().split( )
  A = int(X[0])
  B = int(X[1])
  M = int(math.ceil(math.sqrt(A)))
  N = int(math.ceil(math.sqrt(B))+1)
  C = 0
  
  for j in range(M,N+1):
    if pal(j) == True and pal(j*j) == True and A<=j*j<=B:
        C += 1 
    
  g.write("Case #"+str(i+1)+": "+str(C)+"\n")

