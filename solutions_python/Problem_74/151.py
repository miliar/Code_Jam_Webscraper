import re
input =  open("A-large.in")

class Bot:
  def __init__(self,color,steps):
    self.color = color
    self.position = 1
    self.steps = steps
    self.goals = []
    self.goal_position = 0
    self.goal_order = 0
  def add_next_goal(self,position,order):
    self.goals.append((position,order))
  def move(self,current):
    if self.steps < current:
      return current
    if self.goal_position==0 and len(self.goals)>0:
      (self.goal_position,self.goal_order) = self.goals.pop(0)
    if self.position == self.goal_position:
      if current+1 == self.goal_order:
        # print ("\t%6s: Push Button %d" % (self.color,self.position))
        current += 1
        if len(self.goals) >0:
          (self.goal_position,self.goal_order) = self.goals.pop(0)
      else:  
        pass
        # print "\t%6s: Stay at Button %d" % (self.color,self.position)
    else:
      self.position += 1 if (self.goal_position-self.position > 0) else -1
      # print ("\t%6s: Move to Button %d" % (self.color,self.position))
    return current

T = int(input.readline())
for t in range(1,T+1):
  data = input.readline().split()
  N = int(data[0])
  bots = {'Orange':Bot('Orange',N),'Blue':Bot('Blue',N)}
  order = 1
  for goal in re.findall(r'[OB] \d+'," ".join(data[1:])):
    color = 'Orange' if goal.split(' ')[0]=='O' else 'Blue'
    position = int(goal.split(' ')[1])
    bots[color].add_next_goal(position,order)
    order+=1
  current = 0
  time = 0
  while current < N:
    c1 = bots['Orange'].move(current)
    if current < N:
      c2 = bots['Blue'].move(current)
    current = max(c1,c2)
    time +=1
  print "Case #%d: %d" % (t,time)
