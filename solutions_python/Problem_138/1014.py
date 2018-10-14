f = open('war_data.txt')
T = int(f.readline())
for turn in range(T):
  weights = int(f.readline())
  hers = sorted([float(x) for x in f.readline().split()])[::-1]
  his = sorted([float(x) for x in f.readline().split()])[::-1]
  
  regular = 0
  index = 0
  for i in range(weights):
    if his[index] > hers[i]:
      index += 1
      regular += 1

  deceitful = 0
  index = 0
  for i in range(weights):
    if hers[index] > his[i]:
      index += 1
      deceitful += 1

  print "Case #" + str(turn+1) + ":", deceitful, (weights - regular)