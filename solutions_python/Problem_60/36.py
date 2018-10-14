import sys

for case_index in range(1, 1+input()):

  sys.stderr.write(str(case_index)+' ')
  N,K,B,T=map(int,raw_input().split())
  x=map(int,raw_input().split())
  v=map(int,raw_input().split())
  res = 0
  swaps=0
  c=0
  for k in range(N-1,-1,-1):
    if x[k]+v[k]*T<B:
      swaps+=K-c
    else:
      c += 1
    if c==K:
      break
  if c==K:
    res=swaps
  else:
    res='IMPOSSIBLE'
  print 'Case #%s: %s'%(case_index,res)

sys.stderr.write('\n')
