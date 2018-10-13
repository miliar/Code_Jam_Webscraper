p = 'welcome to code jam'

import sys

def solve(i,j):
  if i==len(p):
    return 1
  if j==len(case):
    return 0
  if memo[i][j]!=-1:
    return memo[i][j]
  res=0
  if p[i]==case[j]:
    res = solve(i+1,j+1)
  res+=solve(i,j+1)
  res%=10000
  memo[i][j]=res
  return res

for case_index in range(1, 1+input()):

  global memo, case
  sys.stderr.write(str(case_index)+' ')
  case = raw_input()
  memo = []
  for x in p:
    memo.append([-1]*len(case))
  res = str(solve(0,0)).zfill(4)
  print 'Case #%s: %s'%(case_index,res)

sys.stderr.write('\n')
