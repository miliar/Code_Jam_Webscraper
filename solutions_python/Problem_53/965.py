
class Snapper():

  def __init__(self, isPoweredOn, state):
    self.isPoweredOn = isPoweredOn
    self.state = state

  def isPowered(self):
    return self.isPoweredOn

  def isOn(self):    
    return self.state
    
  def setPowered(self, isPoweredOn):
    self.isPoweredOn = isPoweredOn

  def setState(self, state):
    self.state = state	  

def snap(N, K):
  snappers = [Snapper(True, False)] + [Snapper(False, False) for i in range(1, N)]

  for i in range(K):
    for idx in range(len(snappers)):
      if snappers[idx].isPowered():
        snappers[idx].setState(not snappers[idx].isOn())

    for idx in range(len(snappers)):
      try:	      
        snappers[idx+1].setPowered(snappers[idx].isOn() and snappers[idx].isPowered())      
      except:
        pass

  return snappers[-1].isOn() and snappers[-1].isPowered()


input = open("A-small-attempt1.in")
output = open("A-small-attempt1.out", "w")

no_of_test_cases = int(input.readline())

for test_case_cnt in range(no_of_test_cases):
  line = input.readline()
  N, K = line.split()
  result = snap(int(N.strip()), int(K.strip()))

  out_line = "Case #" + str(test_case_cnt+1) + ": "  
  if result:
    out_line = out_line + "ON\n"
  else:
    out_line = out_line + "OFF\n"
    
  output.write(out_line)

input.close()
output.close()
