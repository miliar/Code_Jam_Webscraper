from math import ceil

T = int(input())
def ramp(a):
  if a>=0: return a
  else: return 0

def solve(N, M, C, P, B):
  # first find min ride
  #   buyer lower bound
  r_b = max([len(B[b]) for b in B])
  #   front seat lower bound
  # acc sum
  acc_sum = [0]
  for p in range(1, C+1):
    acc_sum.append(acc_sum[-1]+len(P.get(p, [])))
  # print(acc_sum)
  r_p = max([ceil(acc_sum[i]/i) for i in range(1, len(acc_sum))])
  r = max(r_b, r_p)
  # 2. promotion
  prom = 0
  for p in P:
    prom += ramp(len(P[p])-r)
  return r, prom

for i in range(1,T+1):
  N, C, M = map(int, input().split(' '))
  # P, B = [], []
  # for j in range(M):
  #   p, b = map(int, input().split(' '))
  #   P.append(p)
  #   B.append(b)
  PB = []
  B = {}
  P = {}
  for j in range(M):
    p, b = map(int, input().split(' '))
    # PB.append((p, b))
    B.setdefault(b, [])
    B[b].append(p)
    P.setdefault(p, [])
    P[p].append(b)
  ans = solve(N, M, C, P, B)
  print("Case #{}: {} {}".format(i, ans[0], ans[1]))