fileVar = file('A-small-attempt1.in','r')
numTrials = int(fileVar.readline().rstrip())

for z in range(numTrials):
  grid1 = []
  ans1 = 0;
  ans2 = 0;
  ans1 = int(fileVar.readline().rstrip())
  for i in range(4):
    grid1.append(fileVar.readline().rstrip().split())

  ans2 = int(fileVar.readline().rstrip())
  grid2 = []
  for i in range(4):
    grid2.append(fileVar.readline().rstrip().split())
  
  row1 = grid1[ans1-1]
  row2 = grid2[ans2-1]

  answer = -1;
  counter = 0;
  for element in row1:
    if element in row2:
      counter += 1
      answer = "Case #"+str(z+1)+": "+str(element)

  if counter == 0:
    answer = "Case #"+str(z+1)+": Volunteer cheated!"
  elif counter > 1:
    answer = "Case #"+str(z+1)+": Bad magician!"

  print answer


fileVar.close()
