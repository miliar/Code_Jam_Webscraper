T = int(input())
for i in range(1, T + 1):
  D, N = map(int, input().split(' '))
  max_speed = float('inf')
  for j in range(N):
    Ki, Si = map(int, input().split(' '))
    if Ki < D: max_speed = min(max_speed, D * Si / (D - Ki))
  print('Case #{}: {}'.format(i, max_speed))
