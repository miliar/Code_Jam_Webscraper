def tidy(M):
  l=len(str(M))
  s=0
  inc=-1
  p=1
  digits = [int(x) for x in str(M)]
  result = digits
  oops=0

  for i in range(0, l-1):
    if digits[i]>digits[i+1]:
      oops=1
      break
    if digits[i]<digits[i+1]:
      inc=i
    
  for i in range(0, inc):
    result[i]=digits[i]
  if oops==1:
     result[inc+1]=digits[inc+1]-1
     for i in range(inc+2, l):
       result[i]=9
  
  for i in range(0, l):
    s=s+p*result[l-i-1]
    p=p*10
  
  if l==1:
    s=M
  
  return s
  
  
  
t = int(input())  # read a line with a single integer
n=[0]*t
nt=[1]*t

for i in range(0, t ):
  n[i]= int(input())
  nt[i]=tidy(n[i])
  
for i in range(0, t ):
  print("Case #{}: {}".format(i+1, nt[i]))
