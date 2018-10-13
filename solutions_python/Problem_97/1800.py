T = int(raw_input())

def group(l):
  d={}
  for i in l:
    if i in d.keys():
      d[i]+=1
    else:
      d[i]=1
  return d

def gen(n):
  for k in range(10**n):
    l=[(k//(10**i))%10 for i in range(n)]
    flag = False
    for i in range(n-1):
      if l[i]<l[i+1]:
        flag = True
        break
    if flag:continue
    yield l
 
def nor(m,n):
  for k in range(m**n):
    l=[(k//(m**i))%m for i in range(n)]    
    if len(l)==len(group(l)):
      yield l

def cancel(d):
  s = map(str,d)  
  g = group(s)
  return map(eval,g.keys())

def rearrange(l):
  d = []
  a = l[0]
  q = l[1:]
  n = len(q)
  for i in nor(n,n):
    w = map(lambda e:q[e],i)
    d.append([a]+w)
  return cancel(d)

def cycle(l):
  y = []
  for i in range(len(l)):
    y.append(l[i:]+l[:i])
  return y

output = ''

for x in range(T):
  su = 0
  arr = []
  A,B = raw_input().split(' ')
  n = len(A)
  for l in gen(n):
    rs = rearrange(l)
    for r in rs:
      cs = cancel(cycle(r))      
      ks = map(lambda w:''.join(map(str,w)),cs)
      fs = filter(lambda m:len(m)==n and int(m)>=int(A) and int(m)<=int(B),ks)
      g = len(fs)
      m = set(fs)
      if g>=2 and (not m in arr):  
        arr.append(m) 
  for s in arr:  
    g = len(s) 
    su += g*(g-1)/2
  output += 'Case #'+str(x+1)+': '+str(su)+'\n'

print output  
