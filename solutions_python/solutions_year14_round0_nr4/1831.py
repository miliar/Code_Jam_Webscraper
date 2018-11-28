f = open("input.txt","r")
n = int(f.readline())
A = []
B = []
for k in range(n):
   b = int(f.readline())
   N1 = f.readline().strip().split(" ")
   K1 = f.readline().strip().split(" ")
   N2 = [float(N1[i]) for i in range(b)]
   K2 = [float(K1[i]) for i in range(b)]
   N = N2[:]
   K = K2[:]
   s = 0
   for i in range(b):
      m = max(N)
      r = min(K)
      for j in range(b-i):
         if N[j]<m and N[j]>r:
            m = N[j]
      if m > r:
         s+=1
      N.remove(m)
      K.remove(r)
   A = A + [s]
   s = 0
   N = N2[:]
   K = K2[:]
   for i in range(b):
      if max(N) > max(K):
         s+=1
         K.remove(min(K))
      else:
         K.remove(max(K))
      N.remove(max(N))   
   B = B + [s]
f.close()
f = open("output.txt","w")
for k in range(n):
   f.write("Case #"+str(k+1)+": "+str(A[k])+" "+str(B[k])+"\n")
f.close()