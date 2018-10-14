fi=file("input.txt","r")
fo=file("output.txt","w")

def is_palin(n):
  s=str(n)
  if s==s[::-1]: return True
  return False
    
def result(A,B):
  a=int(A**0.5)
  b=int(B**0.5)
  count=0
  if a!=A**0.5: a=a+1 
  for j in range(a,b+1):
    if is_palin(j):
      if is_palin(j**2):
        count=count+1
  return count

T=fi.readline()
for i in range(int(T)):
  numbers=fi.readline()
  num=numbers.strip("\n").split()
  s="Case #"+str(i+1)+": "+str(result(int(num[0]),int(num[1])))
  fo.write(s+"\n")

fi.close()
fo.close()
