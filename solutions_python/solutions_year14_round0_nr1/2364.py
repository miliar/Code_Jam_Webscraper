# Qualification Round Problem A

i = open("A-small-attempt0.in", "r")
o = open("A-small.out", "w")

T = int(i.readline())

for c in range(1, T + 1):
  ans1 = int(i.readline())
  lines1 = []

  for x in range(4):
    lines1.append(i.readline())

  ans2 = int(i.readline())
  lines2 = []

  for x in range(4):
    lines2.append(i.readline())

  line1 = map(int, lines1[ans1 - 1].split(" "))
  line2 = map(int, lines2[ans2 - 1].split(" "))

  matches = []

  for x in line1:
    for y in line2:
      if x == y:
        matches.append(x)

  if len(matches) == 0:
    result = "Volunteer cheated!"
  elif len(matches) > 1:
    result = "Bad magician!"
  else:
    result = matches[0]

  o.write("Case #{0}: {1}\n".format(c, result))

i.close()
o.close()