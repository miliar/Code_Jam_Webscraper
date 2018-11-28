import sys
import pdb
import heapq as hq
from collections import deque, Counter, OrderedDict, defaultdict

pow2 = [1]*51

def printres(casenum, result):
  print "Case #" + str(casenum) + ": " + str(result)
  sys.stdout.flush()


def docase(f,casenum):
  data = f.next().split()
  N = int(data[0])
  P = int(data[1])
  G = 0
  L = pow2[N] - pow2[N-1]
  cnt = 2
  if P == pow2[N]:
    G = pow2[N]-1
  else:
    while P > L:
      L = pow2[N] - pow2[N-cnt]
      cnt += 1
    G = pow2[cnt-1]-2
  L = pow2[N]
  cnt = 1
  while P < L:
    L = pow2[N-cnt]
    cnt += 1
  C = pow2[N] - pow2[cnt-1]
  printres(casenum, str(G) + " " + str(C))

def main():
  for i in xrange(1,51):
    pow2[i] = 2*pow2[i-1]
  with open(sys.argv[1],"r") as f:
    T = int(f.next())
    for k in xrange(T):
      docase(f,k+1)

if __name__ == "__main__":
    main()
