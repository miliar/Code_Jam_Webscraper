import os
f = open("input.txt","r")
n = int(f.readline())
G = []
ch = ""
for k in range(n):
   L = f.readline().split(" ")
   X = int(L[0])
   R = int(L[1])
   C = int(L[2])
   A = min([R,C])
   B = max([R,C])
   if X<7 and A >= X-1 and B >= X and R*C%X == 0:
      ch = "GABRIEL"
   else:
      ch = "RICHARD"
   G = G + [ch]
f = open("output.txt","w")
for k in range(n):
   f.write("Case #"+str(k+1)+": "+G[k]+"\n")
f.close()
