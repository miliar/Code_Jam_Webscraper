import sys

for case_index in range(1, 1+input()):

  sys.stderr.write(str(case_index)+' ')
  N,K=map(int,raw_input().split())
  res = 'ON'
  light=True
  for i in range(1,N+1):
    light &= K%2
    K//=2
  if not light:
    res = 'OFF'
  print 'Case #%s: %s'%(case_index,res)

sys.stderr.write('\n')
