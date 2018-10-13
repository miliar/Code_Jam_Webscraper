import math

t = int(raw_input())  # read a line with a single integer
for i in range(1, t + 1):
  s, k = raw_input().split(" ")
  s = list(s)
  k = int(k)
  flips = 0
  for j in range(len(s)-k+1):
    if s[j] == '-':
      flips += 1
      for q in range(k):
        if s[j+q] == '-':
          s[j+q] = '+'
        else:
          s[j+q] = '-'
  possible = True
  for j in range(k-1):
    if s[-1-j] == '-':
      possible = False
      break

  if possible:
    print("Case #{}: {}".format(i, flips))
  else:
    print("Case #{}: {}".format(i, "IMPOSSIBLE"))
  # check out .format's specification for more formatting options
 
