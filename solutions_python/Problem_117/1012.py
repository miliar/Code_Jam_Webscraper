f = open('lawn', 'r')
lines = f.readlines()
cases = lines[0]
cases = int(cases[:-1])
init=1
for i in range(cases):
  N=int(lines[init].split(' ')[0])
  M=int(lines[init].split(' ')[1])
  #LOADING BOARDS START
  rboard=[]
  cboard=[]
  rfeas=[]
  cfeas=[]
  for n in range(N):
    temp=lines[init+n+1][:-1].split(' ')   
    temp2=[]
    for k in temp:
      temp2.append(int(k))
    rboard.append(temp2)
  for m in range(M):
    temp=[]
    for n in range(N):
      temp.append(int(lines[init+n+1][:-1].split(' ')[m]))
    cboard.append(temp)
  #LOADING BOARDS FINISH

  #CREATE FEASIBILITY ARRAYS START
  for a in rboard:
    temp=[]
    limit=max(a)
    for b in a:
      if b>=limit:
        temp.append(0)
      else:
        temp.append(1)
    rfeas.append(temp)

  for a in cboard:
    temp=[]
    limit=max(a)
    for b in a:
      if b>=limit:
        temp.append(0)
      else:
        temp.append(1)
    cfeas.append(temp)
  #CREATE FEASIBILITY ARRAYS END
  #COPY RFEAS >> FEAS
  feas=[]
  for n in rfeas:
    temp =[]
    for m in n:
      temp.append(m)
    feas.append(temp)
  #END COPY
  #ADD ARRAYS TOGETHER START
  case=0
  for m in range(len(feas)):
    for n in range(len(feas[m])):
      feas[m][n]=feas[m][n]+cfeas[n][m]
      if feas[m][n]>1:
        case=1
  #END ADDITION
  var='YES'
  if case == 1:
    var='NO'

  print 'Case #'+str(i+1)+': '+var

  init=init+N+1   
