def recycle(n,m):
  if(n == m):
    return True
  if(len(str(n)) == len(str(m))):
    templist = list(str(n))
    for x in range(len(str(n))):
      substr = templist[0]
      del templist[0]
      templist+=substr
      if (int(''.join(templist)) == m):
	return True
  return False
    

inputfile = open('C-small-attempt2.in','r').read().split('\n')
T = int(inputfile[0])
del inputfile[0],inputfile[-1]
case=0
while case < T:
  count = 0
  l = inputfile[0].split()
  a = int(l[0])
  b = int(l[1])
  for i in range(a,b+1):
    for j in range(i+1,b+1):
      if(recycle(i,j)):
	count+=1
  del inputfile[0]
  case+=1
  print 'Case #'+str(case)+': '+str(count)
