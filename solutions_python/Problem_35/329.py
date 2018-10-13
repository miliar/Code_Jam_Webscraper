import sys
sys.setrecursionlimit(100000)
filename = sys.argv[1]
f = open(filename)
T = int(f.readline())

def findmin(MAP, r, c):
  global LTR
  ret = [r, c]
  lowest = MAP[r][c]
  d = ((-1, 0), (0, -1), (0, 1), (1, 0))
  for ar, ac in d:
    if r+ar < 0 or r+ar == len(MAP) or c+ac < 0 or c+ac == len(MAP[r]):
      continue
    if MAP[r+ar][c+ac] < lowest:
      ret = [r+ar, c+ac]
      lowest = MAP[r+ar][c+ac]

  return ret

def flow(MAP, r, c):
  global letters, LTR
  #for row in LTR: print ' '.join([str(val) for val in row])
  #print '-' * 15
  if LTR[r][c] != 0:
    return
    
  LTR[r][c] = letters[0]
  lr, lc = findmin(MAP, r, c)
  if lr != r or lc != c:
    #print 'trace min'
    flow(MAP, lr, lc)
    
  d = ((-1, 0), (0, -1), (0, 1), (1, 0))
  for ar, ac in d:
    if r+ar < 0 or r+ar == len(MAP) or c+ac < 0 or c+ac == len(MAP[r]):
      continue
    try:
      rr, rc = findmin(MAP, r+ar, c+ac)
      if rr == r and rc == c:
        #print 'trace max'
        flow(MAP, r+ar, c+ac)
    except:
      pass
  
  return

for M in range(T):
  letters = 'abcdefghijklmnopqrstuvwxyz'
  H, W = f.readline().split()
  H, W = (int(H), int(W))
  MAP = [map(lambda x: int(x), f.readline().split()) for row in range(H)]    
  LTR = [[0 for col in row] for row in MAP]
  for r in range(H):
    for c in range(W):
      #print 'dbg: round %d' % c
      if LTR[r][c] == 0:
        flow(MAP, r, c)
        letters = letters[1:]
  
  print "Case #%d:" % (M+1)
  for row in LTR: print ' '.join(row)