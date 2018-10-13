N = int(raw_input())

def solve(S):
  ans = 0
  cur = 0
  for i,n in enumerate(S):
     need = max(0,i-cur) 
     if need:
       ans += need
       cur = i
     cur += n

  return ans

for i in range(1,1+N):
  Smax,S = raw_input().split()
  print "Case #%d: %d" % (i,solve(map(int,list(S))))
