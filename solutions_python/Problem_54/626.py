f = open('B-small-attempt3.in', 'r')
fout = open('fairwarning.out', 'w')
C = int(f.readline())

for c in range(C):
  s = f.readline().split(' ')
  N = int(s[0])
  tlist = []
  for i in range(N):
    tlist += [int(s[i+1])]
  tlist.sort()
  print tlist
  mindiff = -1
  maxdiff = 0
  for i in range(1,N):
    temp = tlist[i]-tlist[i-1]
    if temp == 0:
      continue
    if temp < mindiff or mindiff == -1:
      mindiff = temp

    if temp > maxdiff:
      maxdiff = temp

  while mindiff != 0:
    rem = maxdiff%mindiff
    maxdiff = mindiff
    mindiff = rem
  gcf = maxdiff
  
  x = tlist[0]%gcf
  if x > 0:
    x -= gcf
    x = -x
  print x
  fout.write('Case #' + str(c+1) + ': ' + str(x) + '\n')
fout.close()
  
    
    
