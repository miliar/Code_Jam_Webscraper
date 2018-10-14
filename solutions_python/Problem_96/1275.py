def doit(filename):
  ifile = open(filename, "rt")
  lines = ifile.readlines()
  ifile.close()
  
  ofile = open("output.txt", "wt")
  for i in range(1, len(lines)):
    ofile.write("Case #" + str(i) + ": ")
    line = lines[i]
    n = int(line[:line.find(" ")])
    line = line[line.find(" ") + 1:]
    s = int(line[:line.find(" ")])
    line = line[line.find(" ") + 1:]
    p = int(line[:line.find(" ")])
    line = line[line.find(" ") + 1:]
    totals = []
    going = True
    while going:
      if line.find(" ") == -1:
        going = False
      totals += [int(line[:line.find(" ")])]
      line = line[line.find(" ") + 1:]
    res = googlers(n, s, p, totals)
    ofile.write(str(res) + "\n")
  ofile.close()

def googlers(n, s, p, totals):
  res = 0
  
  if p == 0:
    minNormalTotal = 0
    minSuprisingTotal = 0
  else:
    minNormalTotal = p * 3 - 2
    if p == 1:
      minSuprisingTotal = 1
    else:
      minSuprisingTotal = p * 3 - 4
  
  for i in range(n):
    if totals[i] >= minNormalTotal:
      res += 1
    elif totals[i] >= minSuprisingTotal:
      if s > 0:
        res += 1
        s -= 1
   
  return res
