import os
f = open("input.txt","r")
n = int(f.readline())
A = []
B = []
for k in range(n):
   num = 0
   p = 0
   L1 = []
   L2 = []
   a = int(f.readline())
   for i in range(1,5):
      st = f.readline()
      if i == a:
         L1 = st.strip().split(" ")
   a = int(f.readline())
   for i in range(1,5):
      st = f.readline()
      if i == a:
         L2 = st.strip().split(" ")
   print(k,L1,L2)
   for i in range(4):
      for j in range(4):
         print(int(L1[i]),int(L2[j]))
         if int(L1[i])==int(L2[j]):
             num = L1[i]
             p+=1
   B = B+[num]
   A = A+[p]
f = open("output.txt","w")
for k in range(n):
   if A[k]==1:
      f.write("Case #"+str(k+1)+": "+str(B[k])+"\n")
   elif A[k]==0:
      f.write("Case #"+str(k+1)+": Volunteer cheated!\n")
   else:
      f.write("Case #"+str(k+1)+": Bad magician!\n")  
f.close()