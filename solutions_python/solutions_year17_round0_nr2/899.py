import os, sys

with open("in.txt") as f:
  lines = [x.strip() for x in f.readlines()]

T = int(lines[0])
for txx in range(T):
  t = txx + 1
  L = len(lines[t])
  num = [int(x) for x in lines[t]]
  norm = True
  for i in range(L):
    if num[i] == 0:
      norm = False
    if num[i] != 1:
      break
  if not norm:
    print("Case #%d: %s" % (t, '9' * (L - 1)))
    continue

  res = ""
  tidy = True
  for i in range(L):
    if not tidy:
      res += '9'
      continue
    for j in range(i, L):
      if num[j] > num[i]:
        break
      if num[j] < num[i]:
        tidy = False
        break
    if not tidy:
      res += str(num[i] - 1)
    else:
      res += str(num[i])
  print("Case #%d: %s" % (t, res))
  