import sys
def read_values():
  return map(int,raw_input().split())

for case_index in range(1, 1+input()):

  m,n = read_values()
  t = []
  for i in range(m):
    t.append(list(raw_input().strip()))
  possible = True
  for i in range(m-1):
    for j in range(n-1):
      if t[i][j]=='#':
        t[i][j]='/'
        possible &= t[i][j+1]=='#'
        possible &= t[i+1][j]=='#'
        possible &= t[i+1][j+1]=='#'
        t[i][j+1]='\\'
        t[i+1][j]='\\'
        t[i+1][j+1]='/'
  for i in range(m):
    for j in range(n):
      possible &= t[i][j]!='#'
  if possible:
    u = [''.join(l) for l in t]
    res = '\n'.join(u)
  else:
    res = 'Impossible'
  sys.stderr.write(str(case_index)+' ')
  print 'Case #%s:\n%s'%(case_index,res)

sys.stderr.write('\n')
