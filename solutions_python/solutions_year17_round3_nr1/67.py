def process(N, K, R, H):
  if K == 1:
    return max([R[j]**2 + 2*R[j]*H[j] for j in range(N)])

  maxarea = -1
  for k in range(N):
    RH = [R[j]*H[j] for j in range(N) if j != k and R[j] <= R[k]]
    if len(RH) >= K-1:
      RH.sort()
      newarea = R[k]*H[k]*2 + R[k]**2 + sum(RH[-(K-1):])*2
      maxarea = max(maxarea, newarea)
  return maxarea

import math

def run():
  T = int(raw_input().strip())

  for caseno in xrange(T):
    N, K = map(int, raw_input().strip().split())
    R, H = zip(*[map(int, raw_input().strip().split()) for _ in range(N)])
    answer = process(N,K,R,H)*math.pi
    print "Case #" + str(caseno+1) + ": " + '{:.10f}'.format(answer)

run()