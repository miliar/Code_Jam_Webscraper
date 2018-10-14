#!/usr/local/bin/python3
    
f = open('input.txt', 'r')
c=[]
n=f.readline()
case=[]
for i in range(int(n)):
  r=[]
  res=[[],[]]
  for j in range(2):
    r=f.readline()
    for k in range(int(r)-1):
      f.readline()
    res[j]=f.readline().rstrip('\n').split(' ')  
    for k in range(4-int(r)):
      f.readline()
  ans=list(set(res[0]) & set(res[1]))
  case.append([len(ans), ans])
cn=1
for i in case:
  s=''
  if i[0]==0:
    s='Volunteer cheated!'
  elif i[0]==1:
    s=i[1][0]
  else:
    s='Bad magician!'
  print('Case #{0}:'.format(cn), s)
  cn=cn+1