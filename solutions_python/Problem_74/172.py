
data = open("A-large.in", "r")
myout = open("robot_out.txt", "w")
cases = int( data.readline() )
  
class World:
  def __init__(self):
    self.clock = 0
    self.current_goal = 0
    self.hurry = False
    self.button_down = False
  
  def passtime(self, amount):
    self.clock += amount
    
class Robot:
  def __init__(self):
    self.position = 1
    self.goals = []
    self.current_goal = 0
  
  def push_da_button(self):
    if world.button_down is False:
      world.current_goal += 1
      world.button_down = True
      self.current_goal += 1
      
  def move_to(self, position):
    if position < self.position:
      self.position -= 1
    elif position > self.position:
      self.position += 1
      
  def update(self, world):
    if self.current_goal >= len(self.goals):
      return 
    (self_goal_id, self_goal_position) = self.goals[self.current_goal]
    if world.current_goal < self_goal_id:
      if self.position != self_goal_position:
        self.move_to( self_goal_position )
      else:
        world.hurry = True
    elif world.current_goal == self_goal_id:
      if self.position != self_goal_position:
        self.move_to( self_goal_position )
      else:
        self.push_da_button()
    else:
      raise Exception("This is not possible!")
      
  def __str__(self):
    rval = ""
    rval += str(self.position) + " " + str(self.current_goal) + " "
    if self.current_goal >= len(self.goals):
      rval += "done"    
    else: 
      rval += str(self.goals[self.current_goal])
    return rval
    
for ct in range(0, cases):
  moves = data.readline().split()
  world = World()
  robohash = {}
  robohash[ 'O' ] = Robot()
  robohash[ 'B' ] = Robot()

  i = 1
  goal_id = 0
  while i < len(moves):
    robot = robohash[ moves[i] ] 
    robot.goals.append( (goal_id, int(moves[i+1] ) ) )
    goal_id += 1
    i += 2
  
  while world.current_goal < goal_id:
    #myout.write( str(robohash['O']) + '\n' )
    #myout.write( str(robohash['B']) + '\n' )
    #myout.write( str(world.current_goal) + '\n' )
    robohash[ 'O' ].update(world)
    robohash[ 'B' ].update(world)
    world.passtime(1)
    world.button_down = False
    #myout.write( str(world.clock) + '\n' )
    #myout.write( "-----" + '\n' )
  
  myout.write( "Case #" + str(ct+1) + ": " + str(world.clock) + '\n' )