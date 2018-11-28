import sys

T=0
N=0
K=0

def read():
  global N
  global K
  line=sys.stdin.readline().strip()
  a=line.split()
  N=int(a[0])
  K=int(a[1])

def calc_max_min(n):
  k=n-1
  return k/2+k%2,k/2

def calc_divider(n):
  power=0
  while  n > (2**power -1) :
    power+=1
  return 2**(power-1)


def solve():
  global N
  global K

  ans=0
  divider=calc_divider(K)
  room=N-divider+1
  a=room/divider
  b=room%divider
  order=K-divider+1
  if order<=b:
    ans=calc_max_min(a+1)
  else:
    ans=calc_max_min(a)

  return ans

T=int(sys.stdin.readline())
for i in xrange(T):
  read()
  ans = solve()
  print "Case #{0}: {1} {2}".format(i+1,ans[0],ans[1])
