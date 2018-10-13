import math

good = ['1', '2', '3']

def find(len, max, zero_allowed = False):
  if len < 0 or max < 0:
    return []
  if len == 0:
    return ['']

  res = []
  start = 1
  if zero_allowed:
    start = 0

  if len == 1:
    while start * start <= max:
      res.append(str(start))
      start = start + 1
    return res

  while 2 * start * start <= max:
    t = find(len - 2, max - 2 * start * start, True)
    t = [str(start) + item + str(start) for item in t]
    res.extend(t)
    start = start + 1
  return res

for L in range(2, 51 + 1):
  good.extend(find(L, 9))

good = [int(item) * int(item) for item in good]

def count(a, b):
  res = 0
  for x in good:
    if x >= a and x <= b:
      res = res + 1
  return res

def get_ints(line):
  line = line.split(" ")
  return [int(item) for item in line]

with open("c.in", "rb") as file:
  tn = int(file.readline())
  for test in range(tn):
    tmp = get_ints(file.readline())
    a = tmp[0]
    b = tmp[1]

    result = count(a, b)
    print "Case #{test}: {result}".format(test = test + 1, result = result)
