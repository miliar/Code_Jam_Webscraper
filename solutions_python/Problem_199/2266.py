import sys

lines = sys.stdin.readlines()
lines = [l[:-1] for l in lines]
T = int(lines[0])

for tc in range(1, T+1):
  pancakes, size = lines[tc].split()
  pancakes = list(pancakes)
  size = int(size)

  ans = 0
  idx = 0
  while idx <= len(pancakes) - size:
    if pancakes[idx] == '-':
      # Flip
      ans += 1
      for i in range(idx, idx + size):
        pancakes[i] = '+' if pancakes[i] == '-' else '-'
    idx += 1

  # Print answer
  if '-' in pancakes:
    print("Case #{0}: IMPOSSIBLE".format(tc))
  else:
    print("Case #{0}: {1}".format(tc, ans))
