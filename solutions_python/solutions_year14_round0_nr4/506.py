import sys

test_cases = int(sys.stdin.readline().strip())

def play_deceitful_war(naomi, ken):
  points = 0
  while len(ken):
    if naomi[0] > ken[0]:
      points += 1
      ken.pop(0)
    else:
      ken.pop()
    naomi.pop(0)
  return points

def play_war(naomi, ken):
  points = 0
  if len(naomi) == 1:
    if naomi[0] > ken[0]:
      return 1
    else:
      return 0

  for block in naomi[:-1]:
    i = len(ken)-1
    j = i
    while i > 0 and ken[i] > block:
      i -= 1

    if i == j and i != 0:
      points += 1
      ken.pop(0)
    elif i == 0 and ken[0] > block:
      ken.pop(0)
    else:
      ken.pop(i+1)

  if naomi[-1] > ken[0]:
    points += 1

  return points

for test_case in range(test_cases):
  sys.stdin.readline()
  naomi_blocks = [float(i) for i in sys.stdin.readline().strip().split(" ")]
  ken_blocks = [float(i) for i in sys.stdin.readline().strip().split(" ")]

  naomi_blocks.sort()
  ken_blocks.sort()

  dec_points = play_deceitful_war(list(naomi_blocks), list(ken_blocks))
  points = play_war(naomi_blocks, ken_blocks)

  print "Case #{0}: {1} {2}".format(test_case+1, dec_points, points)
