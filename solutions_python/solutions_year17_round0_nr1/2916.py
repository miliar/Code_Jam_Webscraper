import sys

def solve(string, k):
  pc = list(string)
  count = 0
  for i in range(0, len(pc) - k + 1):
    if pc[i] == '-':
      for j in range(i, i + k):
        pc[j] = flip(pc[j])
      count += 1
  for i in range(len(pc) - k + 1, len(pc)):
    if pc[i] == '-':
      return 'IMPOSSIBLE'
  return count

def flip(c):
  if c == '-':
    return '+'
  else:
    return '-'

lines = sys.stdin.readlines()
lines.pop(0)
i = 1
for line in lines:
  parts = line.strip().split(' ')
  string = parts[0]
  k = int(parts[1])
  print 'Case #{}: {}'.format(i, solve(string, k))
  i += 1

