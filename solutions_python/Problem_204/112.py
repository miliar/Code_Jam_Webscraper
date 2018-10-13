import sys

N=0
P=0
R=list()
Q=list()

def read():
  global N,P,R,Q
  line=sys.stdin.readline().strip()
  a=line.split()
  N=int(a[0])
  P=int(a[1])
  Q=list()
  line=sys.stdin.readline().strip()
  R=[int(i) for i in line.split()]
  for i in xrange(N):
    line=sys.stdin.readline().strip()
    Q.append([int(j) for j in line.split()])
    Q[i].sort()

def calc(req,val):
  req*=10
  val*=10
  tmax=val/(req/10*9)
  tmin=val/(req/10*11)
  if val % (req/10*11) > 0:
    tmin+=1
  if tmin>tmax:
    return None
  else:
    return tmin,tmax

used=()
def search(index,min_,max_,tmp_used):
  global used
  global N,P,R,Q
  if index >= N:
    return True
  for i in xrange(P):
    if used[index][i]:
      continue
    v=Q[index][i]
    a=calc(R[index],v)
    if a is None:
      continue
    tmax=a[1]
    tmin=a[0]
    if (not tmin >max_) and not( tmax < min_):
      tmp_used.append(i)
      nmax=min(max_,tmax)
      nmin=max(min_,tmin)
      return search(index+1,nmin,nmax,tmp_used)
  return False


def solve():
  global used
  global N,P,R,Q

  used=[[False]*P]*N
  ans=0
  for i in xrange(P):
    tmp_used=list()
    a=calc(R[0],Q[0][i])
    if a is None:
      continue
    tmp_used.append(i)
    if search(1,a[0],a[1],tmp_used):
      ans+=1
      for j in xrange(N):
        used[j][tmp_used[j]]=True
  return ans

        
T=int(sys.stdin.readline())
for i in xrange(T):
  read()
  ans = solve()
  print "Case #{0}: {1}".format(i+1,ans)
