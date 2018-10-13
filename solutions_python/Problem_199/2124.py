import sys

t = int(sys.stdin.readline())
for i in range(1, t + 1):
  ln = sys.stdin.readline().split(" ")
  s = list(ln[0])
  k = int(ln[1])
  flips = 0
  for j in range(0, len(s)-k+1):
      if s[j] == '-':
          flips = flips + 1
          for z in range(j, j+k):
              s[z] = '+' if s[z] == '-' else '-'

  print("Case #{}: {}".format(i, flips if s.count('-') == 0 else 'IMPOSSIBLE'))
