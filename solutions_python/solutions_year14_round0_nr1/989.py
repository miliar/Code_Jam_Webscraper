#!/usr/bin/python3
T = int(input())
for t in range(T):
  print('Case #{}: '.format(t + 1), end='')
  a1 = int(input())
  f1 = [list(map(int, input().split())) for _ in range(4)]
  a2 = int(input())
  f2 = [list(map(int, input().split())) for _ in range(4)]
  ans = -1
  n_ans = 0
  for i in range(1, 17):
    if i in f1[a1 - 1] and i in f2[a2 - 1]:
      ans = i
      n_ans += 1
  if n_ans == 0:
    print('Volunteer cheated!')
  elif n_ans == 1:
    print(ans)
  else:
    print('Bad magician!')

