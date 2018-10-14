

def flip(x):
  if x == '-': return '+'
  return  '-'

def solve(s,k):
  flips = 0
  i = 0
  while i < len(s):
    while i < len(s) and s[i] == '+': i += 1
    if i >= len(s): break
    if i <= len(s)-k:
      flips += 1
      for f in range(k):
        s[i+f] = flip(s[i+f])
    else: return 'IMPOSSIBLE'
  return flips

T = int(input())
for t in range(1, T+1):
  p, k = input().split(' ')
  k = int(k)
  print('Case #{}: {}'.format(t, solve(list(p), k)))

