import sys

p='1 i j k;i -1 k -j;j -k -1 i;k j -i -1'
p=[i.split() for i in p.split(';')]
m={}
for i,a in enumerate('1ijk'):
  for j,b in enumerate('1ijk'):
    m[a+b]=p[i][j]

ps=[]

def prod(a,b):
  r=m[a[-1]+b[-1]]
  if (a[0]=='-')==(b[0]=='-'):
      return r
  if r[0]=='-':
      return r[-1]
  return '-'+r

def check(i,j,r):
  return prod(ps[i+1],r)==ps[j+1]
  
def solve(c):
  global ps
  l,x=list(map(int,raw_input().split()))
  ps=['1']
  s=raw_input()*x 
  for i,a in enumerate(s):
    ps.append(prod(ps[-1],a))
  for i in xrange(l*x-2):
    if ps[i+1]=='i':
      for j in xrange(i+1,l*x-1):
        if check(i,j,'j') and check(j,l*x-1,'k'):
          print('Case #%i: YES'%c)
          return
      break
  print('Case #%i:  NO'%c)
  
if __name__ == '__main__':
  sys.stdin = open('/mnt/sdcard/Download/input.txt', 'r')
  sys.stdout = open('/mnt/sdcard/Download/output.txt', 'w')
  t=int(raw_input())
  for i in range(t):
    solve(i + 1)