from sys import stdin

case_cnt = int(stdin.readline())

R_cache = {}
S_cache = {}

def R(N, K):
  if N == 0: return True
  if (N, K) not in R_cache:
    R_cache[(N, K)] = R(N - 1, K) & S(N - 1, K)
  return R_cache[(N, K)]

def S(N, K):
  if K == 0: return False
  if (N, K) not in S_cache:
    S_cache[(N, K)] = R(N, K - 1) ^ S(N, K - 1)
  return S_cache[(N, K)]

for case_no in range(1, case_cnt + 1):
  N, K   = (int(x) for x in stdin.readline().split())
  N      = N - 1

  result = R(N, K) & S(N, K)
  if result:
    result = 'ON'
  else:
    result = 'OFF'
  print('Case #{}: {}'.format(case_no, result))
