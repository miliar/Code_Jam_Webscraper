def parseInput(fileName): # Parses the input
  h = open(fileName)
  n = int(h.readline())
  res = [] # Array of parsed input
  for i in range(0, n):
    line = h.readline()
    line = line[0:len(line)-1]
    res.append(line.split(" "))
  # Close file and return result
  h.close()
  return res

def generateTrees(params):
  n = int(params[0])
  A = int(params[1])
  B = int(params[2])
  C = int(params[3])
  D = int(params[4])
  x0 = int(params[5])
  y0 = int(params[6])
  M = int(params[7])
  g0 = []
  g1 = []
  g2 = []
  X = x0
  Y = y0
  if X % 3 == 0:
    g0.append((X,Y))
  if X % 3 == 1:
    g1.append((X,Y))
  if X % 3 == 2:
    g2.append((X,Y))
  for i in range(1, n):
    X = (A*X + B) % M
    Y = (C*Y + D) % M
    if X % 3 == 0:
      g0.append((X,Y))
    if X % 3 == 1:
      g1.append((X,Y))
    if X % 3 == 2:
      g2.append((X,Y))
  # Return array
  return [g0, g1, g2]

def findCenter(p1, p2, p3):
  return ((p1[0]+p2[0]+p3[0])/3.0, (p1[1]+p2[1]+p3[1])/3.0)

def solve(params):
  t = generateTrees(params)
  g0 = t[0]
  g1 = t[1]
  g2 = t[2]
  res = 0
  resa = []
  for u in range(0, len(g0)):
    print u
    for v in range(u+1, len(g0)):
      for w in range(v+1, len(g0)):
        if not((g0[u][1]+g0[v][1]+g0[w][1]) % 3):
#          if not((g0[u], g0[v], g0[w]) in set(resa)):
#            resa.append((g0[u], g0[v], g0[w]))
          res += 1

  for u in range(0, len(g1)):
    print u
    for v in range(u+1, len(g1)):
      for w in range(v+1, len(g1)):
        if not((g1[u][1]+g1[v][1]+g1[w][1]) % 3):
#          if not((g1[u], g1[v], g1[w]) in set(resa)):
#            resa.append((g1[u], g1[v], g1[w]))
          res += 1

  for u in range(0, len(g2)):
    print u
    for v in range(u+1, len(g2)):
     for w in range(v+1, len(g2)):
        if not((g2[u][1]+g2[v][1]+g2[w][1]) % 3):
#          if not((g2[u], g2[v], g2[w]) in set(resa)):
#            resa.append((g2[u], g2[v], g2[w]))
          res += 1

  for u in range(0, len(g0)):
    print u
    for v in range(0, len(g1)):
      for w in range(0, len(g2)):
        if not((g0[u][1]+g1[v][1]+g2[w][1]) % 3):
#          if not((g0[u], g1[v], g2[w]) in set(resa)):
#            resa.append((g0[u], g1[v], g2[w]))
          res += 1




  # Return the number
  return res

inputs = parseInput("A-small-attempt1.in") # Parse the input
outputs = ""
for i in range(0, len(inputs)): # Loop over all cases
  outputs += "Case #" + str(i+1) + ": " + str(solve(inputs[i])) + "\n"
# Write output to file
h = open("prob-A.out", "w")
h.write(outputs)
h.close()
