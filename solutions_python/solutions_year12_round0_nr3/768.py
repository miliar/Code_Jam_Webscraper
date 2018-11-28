import sys

def nbValidPermutation(i, maxi):
  strF = str(i)
  nb = 0
  finded = []
  for j in range(len(strF))[:-1]:
    other = int(strF[j+1:]+strF[:j+1])
    if other > i and other <= maxi and not other in finded:
      finded.append(other)
      nb += 1
  return nb

def buildKelem(i, maxi):
  strF = str(i)
  nb = 0
  finded = []
  for j in range(len(strF))[:-1]:
    other = int(strF[j+1:]+strF[:j+1])
    if other > i and other <= maxi and not other in finded:
      finded.append(other)
      nb += 1
  return sorted(finded,reverse=True)

def buildK():
  vals = []
  for i in range(2000000):
    vals.append(buildKelem(i,2000000))
  return vals

def computeSolKno(mini,maxi,kno):
  sol = 0
  for i in range(mini,maxi-1):
    sol += len(kno[i])
    counter = 0
    while counter < len(kno[i]):
      if kno[i][counter] <= maxi:
        counter = len(kno[i])
      else:
        counter += 1
        sol -= 1
  return sol

def computeSol(mini,maxi):
  sol = 0
  for i in range(mini,maxi-1):
    sol += nbValidPermutation(i,maxi)
  return sol

def solve(pathI,pathOut):
  kno = buildK()
  print 'ok, kno'
  counter = 1
  fI = file(pathI,'rU')
  fO = file(pathOut,'w')
  lines = fI.readlines()
  for line in lines[1:]:
    print line
    elem = line.split()
    mini = int(elem[0])
    maxi = int(elem[1])
    sol = computeSolKno(mini,maxi,kno)
    fO.write('Case #')
    fO.write(str(counter))
    fO.write(': ')
    fO.write(str(sol))
    fO.write('\n')
    counter+=1
  fI.close()
  fO.close()
    

def main():
  args = sys.argv[1:]
  solve(args[0],args[1])
  
main()
