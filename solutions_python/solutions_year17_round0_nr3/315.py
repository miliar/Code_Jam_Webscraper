import sys

input = sys.stdin

def solve(n,k):
  #print(n,k)
  p = 0
  while k> 2**p:
    k-=2**p
    p+=1
  if n < 2**(p+1):
    return '0 0'
  lr = []
  #print(k)
  while p>0:
    if k<= 2**(p-1):
      lr.insert(0,0)
    else:
      lr.insert(0,1)
      k-= 2**(p-1)
    p-=1
  #print(lr)  
  gap = n  
  for i in range(len(lr)):
    if gap%2==0 and lr[i] == 1:
      gap= gap//2 -1
      #print('right')
    else:
      gap = gap//2
      #print('left')
  #print(gap)
  if gap%2==0:
    return str(gap//2)+' '+str(gap//2-1)
  else:
    return str(gap//2)+' '+str(gap//2)

for case in range(int(input.readline())):
      values = input.readline().split()
      print("Case #"+ str(case+1) +":", solve(int(values[0]),int(values[1])))
  
