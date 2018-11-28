problem = "B"
inf = open("../data/" + problem + ".in", "r")
outputs = []
outf = open("../data/" + problem + ".out", "w")
datasets = int(inf.readline())
for dataset in range(datasets):
  cfx = inf.readline().strip().split(" ")
  cost = float(cfx[0])
  production = float(cfx[1])
  goal = float(cfx[2])
  rate = 2.0
  time = 0.0
  result = ""
  while not result:
    if (cost / rate) + (goal / (rate + production)) < goal / rate:
      time += cost / rate
      rate += production
    else:
      result = str(time + goal / rate)
  outputs.append("Case #" + str(dataset + 1) + ": " + result)
outf.write("\n".join(outputs))
print "\n".join(outputs)