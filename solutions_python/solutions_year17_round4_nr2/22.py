from sys import stdin

T = int(stdin.readline())
for t in range(T):
  N, C, M = (int(x) for x in stdin.readline().split())
  PB = []
  for _ in range(M):
    PB.append([(int(x) - 1) for x in stdin.readline().split()])

  PM = [0] * N
  BM = [0] * C
  
  for (P,B) in PB:
    PM[P] += 1
    BM[B] += 1

  CPM = [0] * (N + 1)
  for i in range(0, len(PM)):
    CPM[i + 1] = CPM[i] + PM[i]

  y = max(max(BM), max(((n + i - 1) / i) for (i,n) in list(enumerate(CPM))[1:]))
  z = sum(max(0, pm - y) for pm in PM)
  print("Case #%d: %d %d" % (t + 1, y, z))
