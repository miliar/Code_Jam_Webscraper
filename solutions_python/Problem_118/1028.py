import math

def isPalin(n):
  s = str(n)
  for i in range(0, len(s) / 2):
    if s[i] != s[len(s) - i - 1]:
      return False
  return True

def isSquare(n):
  rt = int(math.floor(math.sqrt(n)))
  return (rt * rt == n, rt)

def isFnS(n):
  if isPalin(n):
    rt = isSquare(n)
    if rt[0] and isPalin(rt[1]):
      return True
  return False

lines = []
with open("C-small-attempt0.in", "r") as f:
  for line in f:
    lines.append(line.strip())

N = int(lines[0])
cases = []
for i in range(1, N + 1):
  cases.append(map(lambda x: int(x), lines[i].rsplit()))

output = []
for i in range(0, len(cases)):
  count = 0
  for a in range(cases[i][0], cases[i][1] + 1):
    if isFnS(a):
      count += 1
  output.append("Case #" + str(i + 1) + ": " + str(count))

with open("output.txt", "w") as f:
  for line in output:
    f.write(line + "\n")

