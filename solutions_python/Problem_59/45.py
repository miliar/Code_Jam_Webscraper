import sys

for case_index in range(1, 1+input()):

  sys.stderr.write(str(case_index)+' ')
  N,M=map(int,raw_input().split())
  t = set([raw_input().strip() for i in range(N)])
  u = [raw_input().strip() for i in range(M)]
  res = 0
  for i in range(M):
    w = u[i][1:].split('/')
    p = ''
    for j in range(len(w)):
      p+='/'+w[j]
      if p not in t:
        t.add(p)
        res += 1
    
  print 'Case #%s: %s'%(case_index,res)

sys.stderr.write('\n')
