f = open('input.in', 'r')

lines = f.readlines();
lines.pop(0)

def brut(a,b):
  sol = 0
  for i in range(a,b+1):
    for j in range(i+1, b+1):
      x = str(i)
      y = str(j) + str(j)
      if x in y:
        #print "{0} - {1}".format(x,y)
        sol += 1
  return sol

# Got bored :(
def bun(a,b):
  sol = 0
  for i in range(a, b+1):
    for j in range(i+1, b+1):
      x = str(j) + str(j)
      for nDigits in range(len(str(a)), len(str(b+1))):
        for start in range(str(len(b+1))):
          finish = start + nDigits
          if finish > len(str(b+1)): break
          n = x[start:finish]
          print n
  return sol

for line in range(len(lines)):
  ints = lines[line].split(' ')
  #print ints
  sol = brut(int(ints[0]), int(ints[1]))
  print "Case #{0}: {1}".format(line+1, sol)
