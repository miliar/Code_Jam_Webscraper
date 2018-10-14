import sys
from math import sqrt, floor, ceil

T = int(sys.stdin.readline().strip())

def rdoubs(s):
    p = [s[0]]
    q  =[1]
    for i in s[1:]:
        if(i!=p[-1]):
            p.append(i)
            q.append(1)
        else:
            q[-1]+=1
    return p,q

for trial in range(1, T+1):
  print 'Case #%d:' % trial,
  
  n = [int(x) for x in sys.stdin.readline().strip().split()][0]
  strs = [sys.stdin.readline().strip()]
  nums = [[] for x in range(n)]
  s, nums[0] = rdoubs(strs[0])
  OUT = False
  for i in range(n-1):
    strs.append(sys.stdin.readline().strip())
    si, nums[i+1] = rdoubs(strs[-1])
    if(si != s):
        print "Fegla Won"
        OUT = True
        break
  if(OUT):
    continue
  sums = [0 for i in range(len(s))]  
  

  for i in range(n):
    for j in range(len(s)):
        sums[j] += nums[i][j]
  
  count =0
  for j in range(len(s)):
    k = sums[j] % n
    if(k<n-k):
        z = int(floor(sums[j]/n))
    else:
        z = int(ceil(sums[j]/n))
    for i in range(n):
        count += abs(nums[i][j] - z)

  print count

