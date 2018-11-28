import sys
def read_values():
  return map(int,raw_input().split())

for case_index in range(1, 1+input()):

  sys.stderr.write(str(case_index)+' ')
  a = read_values()
  L = a.pop(0)
  t = a.pop(0)
  N = a.pop(0)
  C = a.pop(0)
  a.extend(range(C,N))
  for i in range(C,N):
    a[i] = a[i%C]
  s = 0
  i = 0
  while i<N and s+2*a[i]<=t:
    s += 2*a[i]
    i += 1
  if i<N:
    a[i] -= (t-s)/2
    a = a[i:]
    a.sort(reverse=True)
    L = min(L,len(a))
    res = t
    for j in range(len(a)):
      if j<L:
        res += a[j]
      else:
        res += 2*a[j]
  else:
    res = s
  print 'Case #%s: %s'%(case_index,res)

sys.stderr.write('\n')
