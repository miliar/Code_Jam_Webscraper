#*-* coding: utf-8 *-*

class SnapperChain(object):
  
  def __init__(self, file):
    self.mode = 'small' if 'small' in file else 'large'
    self.input = open(file, 'r')
    self.testcases = int(self.input.readline().strip())
    self.output = open('/home/ezequiel/output_%s_%s' %(self.__class__.__name__, self.mode), 'w')
    self.toggle_state = []
    self.power_state = []
    
  def main(self):
    for i in range(self.testcases):
      self.toggle_state = []
      self.power_state = []
      self.output.write("Case #%s: " %(i+1))
      N, K = [int(x) for x in self.input.readline().strip('\n').split()]
      self.power_state.append(True)
      for i in range(N):
        self.toggle_state.append(False)
      for i in range(N):
        self.power_state.append(False)
  
      for k in range(K):
        self.toggle_state_copy = self.toggle_state[:]
        self.power_state_copy = self.power_state[:]
        
        for n in range(N):
          if self.power_state_copy[n]:
            self.toggle_state[n] = not self.toggle_state[n]
          self.power_state[n+1] = self.toggle_state[n] and self.power_state[n]

        
      if self.power_state[-1]:
        self.output.write("ON\n")
      else:
        self.output.write("OFF\n")
  
s = SnapperChain('/home/ezequiel/A-small-attempt0.in')
s.main()
