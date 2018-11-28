


def solve(zi):
  s = input()
  k = len(s)
  s = int(s)
  ans = 0
  for i in range(k):
    for dig in range(9, -1, -1):
      if ans + dig * (pow(10, k-i) - 1) / 9 <= s:
        ans += dig * pow(10, k-1-i)
        break
  print('Case #%d: %d'%(zi+1, ans))

zn = int(input())
for zi in range(zn):
  solve(zi)
