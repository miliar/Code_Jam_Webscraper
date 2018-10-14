memo={}
INF=10000
def solve(search_engine,pos,s,q):
  if pos==len(q):
    return 0
  if s[search_engine]==q[pos]:
    return INF
  if memo.__contains__((search_engine,pos)):
    return memo[search_engine,pos]
  else:
    res = INF
    for i in range(len(s)):
      if i==search_engine:
        switch=0
      else:
        switch=1
      res=min(res,switch+solve(i,pos+1,s,q))
    memo[search_engine,pos]=res
    return res


N=int(input())
for step in range(N):
  S=int(input())
  s=[]
  for i in range(S):
    s.append(raw_input())
  Q=int(input())
  q=[]
  for i in range(Q):
    q.append(raw_input())
  memo={}
  res=INF
  for i in range(S):
    res=min(res,solve(i,0,s,q))

  print 'Case #%s: %s'%(step+1,res)
