import sys

def run(t):
  s, n = raw_input().split()
  s = list(s)
  n = int(n)
  result = 0
  for i in range(len(s)):
      if s[i] == '-':
          if i > len(s) - n:
            print('Case #{}: {}'.format(t, 'IMPOSSIBLE'))
            return
          result += 1
          for j in range(n):
              s[i + j] = '+' if s[i + j] == '-' else '-'
  print('Case #{}: {}'.format(t, result))

T = int(raw_input())
for t in xrange(1, T + 1):
  run(t)
