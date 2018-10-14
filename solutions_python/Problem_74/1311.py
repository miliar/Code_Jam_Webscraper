filename = 'A-small-attempt1.in'

BLUE_FIRST = 1
ORANGE_FIRST = 0

def moveRobot(location, destination):
   locationChanged = False
   if(location < destination):
      location += 1
      locationChanged = True
   elif(location > destination):
      location -= 1
      locationChanged = True
   
   return (location, locationChanged)
      
      
      


def compute(data):
   print "****************************************"
   print "COMPUTING LINE:"
   print data
   print "****************************************"
   instructions = data.split(' ')
   # take off the number of instructions
   totalTasks = int(instructions.pop(0))
   OrangeLocation = 1
   BlueLocation = 1
   numberOfMoves = 0
   nextBlueMoveIdx = 0
   nextOrangeMoveIdx = 0
   while(totalTasks > 0):
      numberOfMoves += 1
      try:
         nextOrangeMoveIdx = instructions.index('O')+1
         OrangeLocation, OrangeMoved = moveRobot(OrangeLocation, int(instructions[nextOrangeMoveIdx]))
         moveOrange = True
      except(ValueError):
         print "No Orange Moves Left"
         moveOrange = False
      try:   
         nextBlueMoveIdx = instructions.index('B')+1
         BlueLocation, BlueMoved = moveRobot(BlueLocation, int(instructions[nextBlueMoveIdx]))
         moveBlue = True
      except(ValueError):
         print "No Blue Moves Left"
         moveBlue = False



      # if we find orange first, move him first
      if(moveOrange and nextOrangeMoveIdx < nextBlueMoveIdx or not moveBlue):
         if(OrangeMoved):
            print "Orange moved to " + str(OrangeLocation)
         else:
            totalTasks -= 1
            # remove these two tasks
            instructions.pop(nextOrangeMoveIdx-1)
            instructions.pop(nextOrangeMoveIdx-1)
            print "Orange pushed button " + str(OrangeLocation)
            
         print "Blue moved to " + str(BlueLocation)
      # need to move blue first      
      elif(moveBlue):
         if(BlueMoved):
            print "Blue moved to " + str(BlueLocation)
         else:
            totalTasks -= 1
            # remove these two tasks
            instructions.pop(nextBlueMoveIdx-1)
            instructions.pop(nextBlueMoveIdx-1)
            print "Blue pushed button " + str(BlueLocation)
            

         print "Orange moved to " + str(OrangeLocation)
      else:
         print "Both robots have no moves left, something probably screwed up."
         
   return numberOfMoves
      

      
   

def begin():
   totalMoves = []
   with open(filename) as f: 
      lines = f.readlines()
      print lines
      for line in lines[1:]:
         totalMoves.append(compute(line))

   idx = 0
   for elem in totalMoves:
      idx += 1
      print "Case #" + str(idx) + ": " + str(elem)


