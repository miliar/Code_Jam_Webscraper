def computeSpeed(Ks, Ss):
  max_speed = float('inf')
  for j in range(len(Ks)):
    Ki, Si = Ks[j], Ss[j]
    if Ki < D: max_speed = min(max_speed, D * Si / (D - Ki))
  return max_speed


T = int(input())
for i in range(1, T + 1):
  D, N = map(int, input().split(' '))
  max_speed = float('inf')
  Ks = []
  Ss = []
  for j in range(N):
    Ki, Si = map(int, input().split(' '))
    Ks.append(Ki)
    Ss.append(Si)
  max_speed = computeSpeed(Ks, Ss)
  print('Case #{}: {}'.format(i, max_speed))
