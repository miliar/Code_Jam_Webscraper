import sys, math

iFile = open(sys.argv[1],"r")

size = int(iFile.readline().strip())

for case in range(size):

  richard_wins = False

  line = iFile.readline().strip().split()
  X = int(line[0])
  R = int(line[1])
  C = int(line[2])
  
  if(X > 6):
      richard_wins = True

  if(X > R and X > C):
      richard_wins = True

  if(math.ceil(X/2) > R or math.ceil(X/2) > C):
      richard_wins = True

  if((R*C)%X != 0):
      richard_wins = True

  if(X == 4 and min(R,C) == 2):
      richard_wins = True

  if(X == 6 and min(R,C) == 3):
      richard_wins = True

  if(richard_wins):
      output = "RICHARD"
  else:
      output = "GABRIEL"
  
  print("Case #"+str(case+1)+": "+output)
