import sys
N=int(input())
for step in range(N):
  k=int(input())
  v1=map(int, raw_input().split())
  v2=map(int, raw_input().split())
  v1.sort()
  v2.sort(reverse=True)
  res=0
  for i in range(k):
    res+=v1[i]*v2[i]
  sys.stderr.write(str(step+1)+' ')
  print 'Case #%s: %s'%(step+1,res)
sys.stderr.write('\n')
