f = open(raw_input("Filename: "), 'r')
T = int(f.readline())

Results = []
for x in range(T):
  line = map((lambda x: int(x)), f.readline().split(' '))
  N = line[0]
  S = line[1]
  p = line[2]
  scores = line[3:]
  count = 0
  for score in scores:
    (floored, mod) = divmod(score, 3)
    if mod == 0:
      if floored >= p:
        count += 1
      elif floored + 1 >= p and S > 0 and score >= 3:
        count += 1
        S -= 1
    elif mod == 1 and floored + 1 >= p:
      count += 1
    elif mod == 2:
      if floored + 1 >= p:
        count += 1
      elif floored + 2 >= p and S > 0:
        count += 1
        S -= 1
  Results.append("Case #" + str(x+1) + ": " + str(count))

for x in Results:
  print x
