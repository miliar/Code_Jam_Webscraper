import sys

fin = sys.stdin

T = int(fin.readline())

for case in range(1, T + 1):
  R, k, N = map(int, fin.readline().split())
  #print R, k, N
  G = map(int, fin.readline().split())
  total = 0
  for j in range(0, R):
    #print "j:", j
    for i in range(1, N + 1): #avoid sum[0:0]
      #print "sum:",sum(G[:i])
      if sum(G[:i]) > k:
        #print sum(G[:i-1])
        total += sum(G[:i-1])
        G = G[i-1:] + G[:i-1]
        #print G
	break
      elif i == N:
        total += sum(G)

  print "Case #%d: %d" %(case, total)
