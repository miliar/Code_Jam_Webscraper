import sys

def thing(N,horses,dist):
  cd=[0]# cd[i]=sum_{j<i} dist[j]
  for i in range(N-1): cd.append(cd[-1]+dist[i])
  tim=[[None]*N for i in range(N)]
  # tim[i][j] = min time taken to reach end given at city i arriving on horse j (j<=i)
  for j in range(N): tim[N-1][j]=0
  for i in range(N-2,-1,-1):
    for j in range(i+1):
      t0=t1=1e100
      if horses[j][0]>=cd[i+1]-cd[j]: t0=dist[i]/float(horses[j][1])+tim[i+1][j]
      if horses[i][0]>=cd[i+1]-cd[i]: t1=dist[i]/float(horses[i][1])+tim[i+1][i]
      tim[i][j]=min(t0,t1)
  return tim[0][0]

T=int(sys.stdin.readline())
for case in range(1,T+1):
  [N,Q]=[int(y) for y in sys.stdin.readline().strip().split()]
  horses=[]
  for i in range(N):
    horses.append([int(y) for y in sys.stdin.readline().strip().split()])
  dists=[]
  for i in range(N):
    l=[int(y) for y in sys.stdin.readline().strip().split()]
    if i+1<N: dists.append(l[i+1])
  for i in range(Q):
    dum=sys.stdin.readline()
  print "Case #%d:"%case,thing(N,horses,dists)
