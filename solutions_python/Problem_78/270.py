import os

def divides_evenly(N, P):
  return (N*P) % 100 == 0

def ispossible(N, PD, PG):
  if (PG == 0 and PD != 0) or \
     (PD == 0 and PG != 0):
    return False
  elif PD == PG == 0:
    return True
  for i in xrange(1,N+1):
    if not divides_evenly(i, PD):
      #print i
      continue
    else:
      flag = True
      G = i
      while flag:
        if not divides_evenly(G, PG) or (G*PG < i*PD) or G*(100-PG) < i*(100-PD):
          G += 1
          if G*PG > 10001:
            flag = False
          continue
        else:
          #print i, G, G*PG, i*PD, G*(100-PG), i*(100-PD)
          return True
  return False

def main():
  fin = open("freecell.in", "r", True)
  contents = fin.readlines()
  testcases = int(contents[0].strip())
  for i,case in enumerate(contents[1:]):
    parts = case.split()
    N = int(parts[0])
    PD = int(parts[1])
    PG = int(parts[2])
    if ispossible(N, PD, PG):
      print "Case #%d: Possible" % (i+1)
    else:
      print "Case #%d: Broken" % (i+1)

if __name__ == '__main__':
  main()
