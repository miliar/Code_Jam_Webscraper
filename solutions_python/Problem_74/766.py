import sys

FILENAME = 'A-large.in'  # const string
textReader = open('%s'  % (FILENAME,), 'r')
numTests = int(textReader.readline())

for t in range(1, numTests + 1):
  line = textReader.readline().split(" ")
  n = int(line[0])
  orange = 1
  blue = 1
  solved = False
  time = 1
  orange_goal = 0
  blue_goal = 0
  orange_pos = 1
  blue_pos = 1
  
  end = n*2
  
  
  while not solved:
    #print "Time", time
    while orange_goal == 0 and orange_pos <= end:
      next_color = line[orange_pos].strip()
      orange_pos += 1
      if next_color == "O":
        orange_goal = int(line[orange_pos].strip())
        #print "Orange received next assignment: " + str(orange_goal)
      orange_pos += 1
      #print "Orange_pos:", orange_pos
      
    while blue_goal == 0 and blue_pos <= end:
      next_color = line[blue_pos].strip()
      blue_pos += 1
      if next_color == "B":
        blue_goal = int(line[blue_pos].strip())
        #print "Blue received next assignment: " + str(blue_goal)
      blue_pos += 1
      #print "Blue pos:", blue_pos
      
    if orange == orange_goal:
      #print "Orange reached his goal"
      if orange_pos <= blue_pos:
        #print "Orange pushed button", orange_goal
        orange_goal = 0
      #else:
        #print "Orange is staying put"
      
    if blue == blue_goal:
      #print "Blue reached his goal"
      if blue_pos <= orange_pos:      
        #print "Blue pushed button", blue_goal
        blue_goal = 0
      #else:
        #print "Blue is staying put"
      
      
      
    if orange_goal != 0 and orange != orange_goal:
      if orange < orange_goal:
        orange += 1
      else:
        orange -= 1
      #print "Orange moved to", orange
        
    if blue_goal != 0 and blue != blue_goal:
      if blue < blue_goal:
        blue += 1
      else:
        blue -= 1
      #print "Blue moved to", blue
        
    solved = orange_goal == 0 and blue_goal == 0 and orange_pos >= end and blue_pos >= end
        
    time += 1
    #print
  
  print "Case #" + str(t) + ": " + str(time-1)
  
  
