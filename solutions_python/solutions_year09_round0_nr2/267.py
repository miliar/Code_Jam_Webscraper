import string

def getZones(x,y,h,w,n,t=0):
  zone = [ [x-1,y],[x,y-1],[x,y+1], [x+1,y]]
  d = []
  for i in zone:
    (a,b) = i
    if t == 1:
      if a < 0 or a > h-1 or b < 0 or b > w-1 or n[a][b]!="":
        d.append(i)
    else:
      if a < 0 or a > h-1 or b < 0 or b > w-1:
        d.append(i)

  for i in d:
    zone.remove(i)
  return zone

def min(h,w,m,n,q,x,y,l):
  zone = getZones(x,y,h,w,n)
  min = m[x][y]
  u = [-1,-1]
  for i in zone:
    (a,b) = i
    if min > m[a][b]:
      min = m[a][b]
      u = [a,b]
  return u

def unde(h,w,m,n,q,x,y,l):
  u = min(h,w,m,n,q,x,y,l)
  if u != [-1,-1]:
    (a,b) = u
    if n[a][b] == "":
      n[a][b]=l
      q.append(u)
  return (n,q)

def deunde(h,w,m,n,q,x,y,l):
  zone = getZones(x,y,h,w,n,1)
  for i in zone:
    (a,b) = i
    u = min(h,w,m,n,q,a,b,l)
    if u == [x,y]:
      if n[a][b] == "":
        n[a][b]=l
        q.append([a,b])
  return (n,q)

def scan(n,h,w):
  for i in range(h):
    for j in range(w):
      if n[i][j] == "":
        return [i,j]

def job(case,g):
  letters = [ i for i in string.lowercase]
  lc = 0
  l = letters[lc]

  a = f.readline().rstrip("\n").split(" ")
  (h,w) = map(lambda x: int(x),a)

  m = []
  n = []

  for i in range(h):
    a = f.readline().rstrip("\n").split(" ")
    a = map(lambda x: int(x),a)
    m.append(list(a))
    n.append([ "" for i in range(len(list(a)))])

  max = h*w
  c = 0
  Q = []
  n[0][0]=l
  Q.append([0,0])

  while c < max:
    for i in Q:
      (oo,ou) = i
      (n,Q)=unde(h,w,m,n,Q,oo,ou,l)
      (n,Q)=deunde(h,w,m,n,Q,oo,ou,l)
    c += len(Q)
    if c < max:
      del(Q)
      Q = []
      next = scan(n,h,w)
      lc += 1
      l = letters[lc]
      n[next[0]][next[1]]=l
      Q.append(next)

  g.write("Case #"+str(case+1)+":\n")
  for i in range(h):
    a = map(lambda x: str(x),n[i])
    a = string.join(a," ")
    g.write(a+"\n")
###

f = open("input.in","r")
g = open("input.out","w")
t = int(f.readline().rstrip("\n"))

for i in range(t):
  job(i,g)
