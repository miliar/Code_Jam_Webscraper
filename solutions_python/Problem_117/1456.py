import numpy as np

debug = False

def readMatrix(N, M, dtype=np.int16):
  a = [None] * N
  for i in range(N):
    line = raw_input()
    a[i] = [int(x) for x in line.split()]
  return np.array(a, dtype=dtype)


def verifyPattern(a):
  # * For each cell a[i, j]
  for i in range(a.shape[0]):
    for j in range(a.shape[1]):
      # ** If a[i, j] is the row min or col min, every cell in either its row or col must be equal to a[i, j]
      if debug: print "verifyPattern(): a[{}, {}] = {}, row min = {}, col. min = {}".format(i, j, a[i, j], min(a[i, :]), min(a[:, j]))
      if a[i, j] == min(a[i, :]) or a[i, j] == min(a[:, j]):
        if not (np.all(a[i, :] == a[i, j]) or np.all(a[:, j] == a[i, j])):
          return "NO"
  
  return "YES"


def lawnmower():
  T = int(raw_input())
  for case in range(T):
    if debug: print "\nlawnmower(): Case #{}".format(case + 1)
    
    line = raw_input()
    #if debug: print "lawnmower(): line = {}".format(line)
    
    N, M = tuple(int(x) for x in line.split())
    #if debug: print "lawnmower(): N = {}, M = {}".format(N, M)
    
    a = readMatrix(N, M, dtype=np.uint8)
    if debug: print "lawnmower(): a ({}x{}):-\n{}".format(N, M, a)
    
    result = verifyPattern(a)
    print "Case #{}: {}".format(case + 1, result)

if __name__ == "__main__":
  lawnmower()
