import sys
import re

L,D,N = [int(i) for i in raw_input().split()]
tokens = []
for i in range(D):
  tokens.append(raw_input())

lines = []
for i in range(N):
  lines.append(raw_input())

pt = re.compile('\(([a-z]+)\)|([a-z])')

for i,line in enumerate(lines):
  ans = 0
  ptn = [(l or r) for l,r in pt.findall(line)]
  for dword in tokens:
    ans += all([d in p for d, p in zip(dword, ptn)])
  print "Case #%d: %d" % (i+1, ans)
