t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  pancakes, K = input().split(' ')
  K = int(K)
  N = len(pancakes)
  changes = []
  last = '+'
  for p in pancakes:
    if p == last:
      changes.append(0)
    else:
      changes.append(1)
    last = p
  changes.append(0) # guard
  flips = 0
  for j in range(N-K+1):
    if changes[j] == 1:
      flips = flips + 1
      changes[j] = 1 - changes[j]
      changes[j + K] = 1 - changes[j + K]
  impossible = False
  for j in range(N-K+1, N):
    if changes[j] == 1:
      impossible = True
      break
  result = 'IMPOSSIBLE' if impossible else flips
  print("Case #{}: {}".format(i, result))
  