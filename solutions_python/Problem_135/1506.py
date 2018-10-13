import sys

tests = int(sys.stdin.readline())

for i in range(0, tests):
  first = int(sys.stdin.readline())
  arrangment = []

  for j in range(0, 4):
    line = sys.stdin.readline()
    arrangment.append([int(n) for n in line.split()])

  possible = arrangment[first - 1]

  second = int(sys.stdin.readline())

  arrangment = []

  for j in range(0, 4):
    line = sys.stdin.readline()
    arrangment.append([int(n) for n in line.split()])

  answer = [n for n in arrangment[second - 1] if n in possible]
  
  if len(answer) == 1:
    msg = str(answer[0])
  elif len(answer) == 0:
    msg = "Volunteer cheated!"
  else:
    msg = "Bad magician!"

  print "Case #%d: %s" % ((i + 1), msg)
