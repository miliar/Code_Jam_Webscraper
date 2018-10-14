import sys
def solve(n):
  s=map(int, str(n))
  while True:
    i = find(s)
    if i == -1: break
    s[i-1] -= 1
    for j in range(i, len(s)):
      s[j] = 9
  return int("".join(map(str, s)))

def find(s):
  for i in range(1, len(s)):
    if s[i - 1] > s[i]:
      return i
  return -1


t=input()
for i in range(t):
  n=input()
  print "Case #%d: %d" % (i + 1, solve(n))
