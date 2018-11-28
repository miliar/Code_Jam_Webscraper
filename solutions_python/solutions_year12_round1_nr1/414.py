def do(filename):
  ifile = open(filename, "rt")
  lines = ifile.readlines()
  ifile.close()
  num = 1
  
  ofile = open("output.txt", "wt")
  for i in range(1, len(lines), 2):
    ofile.write("Case #" + str(num) + ": ")
    line = lines[i]
    a = int(line[:line.find(" ")])
    line = line[line.find(" ") + 1:]
    b = int(line)
    
    line = lines[i + 1]
    probs = []
    going = True
    while going:
      if line.find(" ") == -1:
        going = False
      probs += [float(line[:line.find(" ")])]
      line = line[line.find(" ") + 1:]
    
    res = keystrokes(a, b, probs)
    ofile.write(str(res) + "\n")
    
    num += 1
  ofile.close()

def keystrokes(typed, total, probs):
  res = total + 2
  
  for backspaces in range(0, typed):
    need = typed - backspaces
    
    goodChance = 1
    for prob in probs[:need]:
      goodChance *= prob
    badChance = 1 - goodChance
    
    goodCount = (backspaces * 2) + (total - typed) + 1
    badCount = goodCount + total + 1
    
    expected = goodChance * goodCount
    expected += badChance * badCount
    
    if expected < res:
      res = expected
  
  return res
