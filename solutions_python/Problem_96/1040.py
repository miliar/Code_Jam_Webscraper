import math

def votes(n):
  v=[0,0,0]
  v[0]=int(n/3)
  n=n-v[0]
  v[1]=int(n/2)
  n=n-v[1]
  v[2]=n
  return v

def mvote(n):
  return int(math.ceil(n/3.0))

def smvote(n):
  if (n==0):
    return 0
  return int(round(n/3.0))+1

def svotes(n):
  v=[0,0,0]
  v[0]=int(round(n/3.0))+1
  while (v[0]>10):
    v[0]=v[0]-1
  n=n-v[0]
  v[1]=int(n/2)
  n=n-v[1]
  v[2]=n
  return v


f = open('input.dat')
n=f.readline()
n=int(n)
for q in range(n):
  count=0
  sline=[]
  line=f.readline()
  line=line.split(' ')
  line=[int(j) for j in line]
  m=line.pop(0)
  s=line.pop(0)
  p=line.pop(0)
  for k in range(m):
    if(mvote(line[k])>=p):
      count=count+1
    else:
      sline.append(line[k])

  for k in range(len(sline)):
    sline[k]=smvote(sline[k])
  sline.sort()
  sline.reverse()
  for i in range(s):
    try:
      if (sline[i]>=p):
        count=count+1
    except:
      a=0
  print "Case #"+str(q+1)+": "+str(count)
    













