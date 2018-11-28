problem = "A"
inf = open("../data/" + problem + ".in", "r")
outputs = []
outf = open("../data/" + problem + ".out", "w")
datasets = int(inf.readline())
for dataset in range(datasets):
  row = int(inf.readline())
  items = []
  for i in range(4):
    if i + 1 == row:
      items = inf.readline().strip().split(" ")
    else:
      inf.readline()
  new_row = int(inf.readline())
  new_items = []
  for i in range(4):
    if i + 1 == new_row:
      new_items = inf.readline().strip().split(" ")
    else:
      inf.readline()
  matched = 0
  for new_item in new_items:
    if new_item in items:
      matched += 1
      match = new_item
  if matched == 0:
    result = "Volunteer cheated!"
  elif matched == 1:
    result = match
  else:
    result = "Bad magician!"
  outputs.append("Case #" + str(dataset + 1) + ": " + result)
outf.write("\n".join(outputs))
print "\n".join(outputs)