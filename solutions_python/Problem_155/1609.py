import os
f = open("input.txt","r")
n = int(f.readline())
R = []
for k in range(n):
   L = f.readline().split(" ")
   s = int(L[0])
   r = 0
   ch = L[1]
   p = 0
   for i in range(s+1):
      if p<i:
         r = r + i - p
         p = i
      p = p + int(ch[i])
   R = R + [r]
f = open("output.txt","w")
for k in range(n):
   f.write("Case #"+str(k+1)+": "+str(R[k])+"\n")
f.close()
