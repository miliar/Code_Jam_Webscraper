import sys
data = sys.stdin.readlines()


i=1
while ( i < len(data)):
  line = data[i]
  inputs = line.split()
  surprising = int(inputs[1])
  p = int(inputs[2])
  possible = 0
  x = 3
  while x < len(inputs):
    c = int(inputs[x])

    if c == 0 and p > 0:
      x = x+1
      continue

    if c >= 0 and p == 0:
      possible = possible +1
      x=x+1
      continue

    if c / p >= 3:
      possible = possible + 1
      x = x+1
      continue

    if abs(c - (p+p+p)) <=2:
      possible = possible +1
      x = x+1
      continue

    if surprising > 0:
      if abs(c - (p*3)) <= 4:
        possible = possible+1
        surprising = surprising -1
    x = x+1
    
  
  print "Case #" + str(i) + ": " + str(possible)
  i=i+1
  
  
