
import sys
fi=open(sys.argv[1],"r")
fo=open(sys.argv[2],"w")

tests=int(fi.readline())

BASES=10
MAX=10**6

basic=[False,True]+[-1]*MAX
dp=[]
for i in range(BASES+1):
  dp.append(basic[:])

def s(x,base):
  ret=0
  while x>0:
    ret+=(x%base)**2
    x/=base
  return ret

def is_happy(x,base):
  global dp
  if(dp[base][x] is not -1): return dp[base][x]
  dp[base][x]=False
  n=s(x,base)
  ret=is_happy(n,base)
  dp[base][x]=ret
  return ret

for i in range(tests):
  line=map(int,fi.readline().split())
  j=2
  while True:
    ok=True
    for k in line:
      if not is_happy(j,k):
        ok=False
        break
    if ok:
      fo.write("Case #%d: %d\n"%(i+1,j))
      break
    j+=1

fi.close()
