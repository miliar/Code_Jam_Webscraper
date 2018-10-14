infile = open('B-small-attempt3.in','r')
outfile = open('B-small.out','w')

C = int(infile.readline().strip('\n'))

for c in range(1,C+1):
  print c
  line = infile.readline().strip('\n')
  tokens = line.split()
  N=int(tokens[0])
  tokens=tokens[1:]
  gaps = []
  for i in range(0,N):
    for j in range(0,N):
      if i != j:
        gap = abs(int(tokens[i])-int(tokens[j]))
        if gap not in gaps:
          gaps.append(gap)
  gaps.sort()
  highest = gaps[0]
  if(highest == 0):
    highest = gaps[1]
  factor = False
  while not factor and highest > 0:
    factor = True
    for gap in gaps:
      if gap % highest != 0:
        highest -= (gap % highest)
        factor = False
        break
  t = int(tokens[0])
  y=0
  if t % highest == 0:
    y = 0
  elif t < highest:
    y=highest-t
  elif t > highest:
    y = (t/highest + 1) * highest -t
  
  outfile.write("Case #" + str(c) + ": " + str(y) + "\n")

outfile.close()
infile.close()