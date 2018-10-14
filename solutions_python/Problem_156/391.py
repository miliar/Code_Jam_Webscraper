import sys

def solve(c):
  d=int(raw_input())
  p=list(map(int,raw_input().split()))
  ans=10**9
  for s in xrange(1,max(p)+1):
    tans=s
    for x in p:
      if x > s:
        tans+=(x+s-1)/s-1
    ans=min(ans,tans)
  print('Case #%i: %i'%(c,ans))

if __name__ == '__main__':
  sys.stdin = open('/mnt/sdcard/Download/input.txt', 'r')
  sys.stdout = open('/mnt/sdcard/Download/output.txt', 'w')
  t=int(raw_input())
  for i in range(t):
    solve(i + 1)