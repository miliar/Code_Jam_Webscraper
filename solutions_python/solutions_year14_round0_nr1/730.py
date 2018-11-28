

def solve(test, f):
  res = "Bad magician!"
  
  rowA = int(f.readline().strip())
  linesA = []
  for i in range(4):
    r = f.readline().split()
    r = [int(x.strip()) for x in r]
    linesA.append(r)
  
  rowB = int(f.readline().strip())
  linesB = []
  for i in range(4):
    r = f.readline().split()
    r = [int(x.strip()) for x in r]
    linesB.append(r)
    
  setA = set(linesA[rowA-1])
  setB = set(linesB[rowB-1])
  inters = setA.intersection(setB)
  
  if len(inters) == 0:
    res = "Volunteer cheated!"
  elif len(inters) > 1:
    res = "Bad magician!"
  else:
    res = list(inters)[0]
  
  print "Case #" + str(test+1) + ": " + str(res)


if __name__ == '__main__':
  f = open('A.in', 'r')
  T = int(f.readline().strip())
  for i in range(T):
    solve(i, f)
