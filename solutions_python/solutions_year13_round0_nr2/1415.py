#!/usr/bin/python2

class Lawn:

  # table is a 16-char line holding the state
  def setLawn(self, lawn, n, m):
    self.lawn = lawn
    self.n = n
    self.m = m

    # Holds the current state of the lawn
    self.state = []

    # Initialize state vector
    for a in range(n*m):
      self.state.append(100)

  # Cuts with the maximum possible height
  def cutRows(self):

    # Find the maximum height in a row and cut it
    for r in range(self.n):

      height = 0
      for c in range(m):
        #if self.lawn[r*m] < self.lawn[r*m + c]:
        if self.lawn[r*m + c] > height:
          height = self.lawn[r*m+c]

      # Cut
      for c in range(m):
        #Only cut if the value is greater than height
        if self.state[r*m+c] > height:
          self.state[r*m+c] = height

  def cutCols(self):

    # Find the maximum height in a col and cut it
    for c in range(self.m):

      height = 0
      for r in range(n):
        #if self.lawn[r*m] < self.lawn[r*m + c]:
        if self.lawn[r*m + c] > height:
          height = self.lawn[r*m+c]

      # Cut
      for r in range(n):
        #Only cut if the value is greater than height
        if self.state[r*m+c] > height:
          self.state[r*m+c] = height
      #print "max height in "+str(r)+" row: "+str(height)
  
  def debugPrint(self):
    for r in range(n):
      for c in range(m):
        print self.state[r*m + c],

      print '\n',

  def yesORno(self):
    #Compare every lawn patch
    for r in range(n):
      for c in range(m):
        if self.state[r*m + c] != self.lawn[r*m + c]:
          return False


    return True

if __name__ == "__main__":

  l = Lawn()

  f = open('sample', 'r')

  # Number of samples
  n = f.readline()

  for i in range(int(n)):
    
    # Read N and M
    #[n, m] = f.readline().split(' ')
    fl =  f.readline().replace('\n', '').split(' ')
    n = int(fl[0])
    m = int(fl[1])

    lawn = []
    
    # For each line
    for a in  range(int(n)):

      # Append a value
      for value in f.readline().replace('\n', '').split(' '):
        #lawn += f.readline()
        lawn.append(int(value))

    l.setLawn(lawn, n, m)

    l.cutRows()
    l.cutCols()

    if l.yesORno() == True:
      print "Case #"+str(i+1)+": YES"
    else:
      print "Case #"+str(i+1)+": NO"
