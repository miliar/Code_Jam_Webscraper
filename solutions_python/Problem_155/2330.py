import math
import csv

def Friends(A):
  count=0
  sum=0
  for i in range(1,len(A)):
    sum+=A[i-1]
    if count+sum<i:
      count+=(i-sum-count)
  return count

def Decompose(n,A):
  B=A
  L=[]
  for i in range(n+1):
    L.append(B%10)
    B=B//10
  L.reverse()
  return L

f=open("Input A - Large.txt")
g=open("Output A - Large.txt",'w')
reader=csv.reader(f,delimiter=" ")
writer=csv.writer(g)
count=0
for row in reader:
  if count==0:
    c=count
    count+=1
    continue
  L=list(row)
  L[0]=int(L[0]); L[1]=int(L[1],10)
  M=Decompose(L[0],L[1])
  g.write("Case #"+str(count)+": "+str(Friends(M))+"\n")
  count+=1
f.close()
g.close()
  


