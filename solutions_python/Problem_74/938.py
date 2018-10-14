import os
import sys

class Solver(object):
  pos = None
  count = 0
  
  bp = 1
  op = 1
  
  def __init__(self, input):
    self.pos = input
    
  def next(self):
    bpressed = False;
    # print 'next ' + str(self.count) 
    if len(self.pos) == 0:
      return False
      
    self.count = self.count + 1
    
    if self.bp == self.getNextBP():
      if self.isNextB():
        self.pressB()
        bpressed = True
    else:
      self.moveB()
      
      
    if self.op == self.getNextOP():
      if self.isNextO() and not bpressed:
        self.pressO()
    else:
      self.moveO()
      
    return True
      
  def getNextBP(self):
    if 'B' not in self.pos: return self.bp
    nextB = self.pos.index('B')
    return int(self.pos[nextB+1])
    
  def isNextB(self):
    if 'B' not in self.pos:
      return False;

    if 'O' not in self.pos:
      return True;

    return self.pos.index('B') < self.pos.index('O')
    
  # assumes B is at the head
  def pressB(self):
    # print '\tpress b'
    self.pos = self.pos[2:]
    
  def moveB(self):
    # print '\tmove b'
    pos = self.getNextBP()
    if pos > self.bp:
      self.bp += 1
    elif pos < self.bp:
      self.bp-=1
        
  def getNextOP(self):
    if 'O' not in self.pos: return self.op
    nextB = self.pos.index('O')
    return int(self.pos[nextB+1])
    
  def isNextO(self):
    if 'O' not in self.pos:
      return False;
    
    if 'B' not in self.pos:
      return True
      
    return self.pos.index('O') < self.pos.index('B')
  
  # assumes O is at the head
  def pressO(self):
    # print '\tpress o'
    self.pos = self.pos[2:]
    
  def moveO(self):
    # print '\tmove o'
    pos = self.getNextOP()
    if pos > self.op:
      self.op += 1
    elif pos < self.op:
      self.op -= 1

solutions = []

num = int(sys.stdin.readline().strip())

for i in xrange(num):
  s = Solver(sys.stdin.readline().strip().split()[1:])

  while s.next():
    pass
  
  solutions.append(s.count)

for i in xrange(num):
  print 'Case #' + str(i+1) + ': ' + str(solutions[i])

