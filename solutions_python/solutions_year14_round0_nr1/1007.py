def getArray(index):
  rows = []
  for i in xrange(4):
    rows.append(map(int, raw_input().split()))
  return rows[index]


for t in xrange(int(raw_input())):
  row = int(raw_input()) - 1
  first = set(getArray(row))
  row = int(raw_input()) - 1
  second = set(getArray(row))
  result = first.intersection(second)
  if len(result) == 0:
    answer = "Volunteer cheated!"
  elif len(result) > 1:
    answer = "Bad magician!"
  else:
    answer = str(result.pop())
  print "Case #" + str(t + 1) + ": " + answer
