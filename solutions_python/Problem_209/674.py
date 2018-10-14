import math
pi = math.pi

pancakes = []

# best sum whose last element is pc i

def f(K, i):
  global memo
  if memo[K][i] != -1:
    return memo[K][i]
  if K == 1:
    res = pancakes[i][1] * pancakes[i][0]
  else:
    res = 0
    for j in range(0,i):
      res = max(res, pancakes[i][1] * pancakes[i][0] + f(K-1,j))
  memo[K][i] = res
  return res

T = int(input())
for i in range(T):
  N, K = map(int, input().split())
  pancakes = []
  memo = [[-1 for i in range(1001)] for i in range(1001)]
  for j in range(N):
    R, H = map(int, input().split())
    pancakes = pancakes + [(R,H)]
  pancakes.sort()
  l = [2 * pi * f(K,i) + pancakes[i][0] ** 2 * pi for i in range(0,N)] 
  res = max(l)
  print("Case #", i + 1, ": ", res, sep = '')
