import sys

def parseProblem(problem):
  splits = problem.rstrip().split(' ')
  
  orange = []
  blue = []
  ordering = []
  
  numberOfButtonPresses = splits.pop(0)
  
  current = None
  for split in splits:
    if split == 'O':
      current = orange
      ordering.append(split)
    elif split == 'B':
      current = blue
      ordering.append(split)
    else:
      current.append(int(split))

  return (orange, blue, ordering)
  
def solveProblem(problem):
  orange, blue, ordering = problem
  
  orangeAt = 1
  blueAt = 1
  
  result = 0
  
  length = len(ordering)
  while len(ordering) > 0:
    result += 1
    #printLine = str(result) + ' | '
    
    if len(orange) > 0 and orangeAt == orange[0] and ordering[0] == 'O':
      del orange[0]
      del ordering[0]
      #printLine += 'Orange pressed button at[' + str(orangeAt) + '], '
      
      if len(blue) > 0:
        #printLine += 'Blue moving from[' + str(blueAt) + '] to ['
        if blueAt > blue[0]:
          blueAt -= 1
        elif blueAt < blue[0]:
          blueAt += 1
        #printLine += str(blueAt) + '], '
    elif len(blue) > 0 and blueAt == blue[0] and ordering[0] == 'B':
      del blue[0]
      del ordering[0]
      #printLine += 'Blue pressed button at[' + str(blueAt) + '], '
      
      if len(orange) > 0:
        #printLine += 'Orange moving from[' + str(orangeAt) + '] to ['
        if orangeAt > orange[0]:
          orangeAt -= 1
        elif orangeAt < orange[0]:
          orangeAt += 1
        #printLine += str(orangeAt) + '], '
    else:
      if ordering[0] == 'O':
        orangeTime = abs(orangeAt - orange[0])
        orangeAt = orange[0]

        if len(blue) > 0:
          blueTime = abs(blueAt - blue[0])
          if blueTime <= orangeTime:
            blueAt = blue[0]
          else:
            if blueAt < blue[0]:
              blueAt += orangeTime
            elif blueAt > blue[0]:
              blueAt -= orangeTime
              
        result += orangeTime - 1
      elif ordering[0] == 'B':
        blueTime = abs(blueAt - blue[0])
        blueAt = blue[0]
        
        if len(orange) > 0:
          orangeTime = abs(orangeAt - orange[0])
          if orangeTime <= blueTime:
            orangeAt = orange[0]
          else:
            if orangeAt < orange[0]:
              orangeAt += blueTime
            elif orangeAt > orange[0]:
              orangeAt -= blueTime

        result += blueTime - 1
          
  return result

inputFile = 'input.txt'
outputFile = 'output.txt'

file = open(inputFile, 'r')

numberOfProblems = file.readline()
problems = file.readlines()

file.close()

file = open(outputFile, 'w')

count = 1
for problem in problems:
  file.write('Case #' + str(count) + ': ' + str(solveProblem(parseProblem(problem))) + '\n')
  count += 1