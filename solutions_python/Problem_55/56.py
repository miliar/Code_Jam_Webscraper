import sys

for case_index in range(1, 1+input()):

  R,k,N = map(int,raw_input().split())
  g = map(int,raw_input().split())
  start = []
  loads = []
  i = 0
  euros = 0
  for r in range(N+1):
    start.append(i)
    load = 0
    ngroups = 0
    while load+g[i]<=k and ngroups<N:
      load += g[i]
      i += 1
      i %= N
      ngroups += 1
    loads.append(load)

  s = -1
  for i in range(len(start)):
    for j in range(i+1,len(start)):
      if start[i]==start[j] and s==-1:
        period = j-i
        s = i
  res=0
  nsteps = min(R,s)
  for i in range(nsteps):
    R-=1
    res+=loads[i]

  q = R/period
  RR = R%period
  res += q*sum(loads[s:s+period])+sum([loads[s+r] for r in range(RR)])

  sys.stderr.write(str(case_index)+' ')
  print 'Case #%s: %s'%(case_index,res)

sys.stderr.write('\n')

