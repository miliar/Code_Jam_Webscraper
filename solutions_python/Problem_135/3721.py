io = open("input.txt", "r")
ot = open("output.txt", "w+")

t = int(io.readline())

for i in range(t):
  a1 = int(io.readline())
  g1 = []
  for j in range(4):
    l = io.readline().split()
    g1.append(l)
  a2 = int(io.readline())
  g2 = []
  for j in range(4):
    l = io.readline().split()
    g2.append(l)
  
  r1 = g1[a1-1]
  r2 = g2[a2-1]
  
  sol = (list(set(r1).intersection(r2)))
  
  if (len(sol) == 1):
    ot.write("Case #" + str(i+1) + ": " + sol[0] + "\n")
  elif (len(sol) > 1):
    ot.write("Case #" + str(i+1) + ": Bad magician!\n")
  elif (len(sol) == 0):
    ot.write("Case #" + str(i+1) + ": Volunteer cheated!\n")

io.close()
ot.close()
