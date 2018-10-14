import sys

"""
sequence = [('O', 2), ('B', 1), ('B', 2), ('O', 4)]


o_seq = [(2, 0), (4, 3)]
b_seq= [(1, 1), (2, 2)]

sequence = [('O', 5), ('O', 8), ('B', 100)]
sequence = [('B', 2), ('B', 1)]
"""
class RobState(object):
  def __init__(self, seq):
    self.split_seq(seq)
    self.b_loc = 1
    self.o_loc = 1
    self.b_curr = 0
    self.o_curr = 0

    self.time = 0
    self.comp = 0
    self.seq = seq

  def split_seq(self, seq):
    self.o_seq = []
    self.b_seq = []
    i = 0
    for robot, button in seq:
      if robot == 'O':
        self.o_seq.append((button, i))
      elif robot == 'B':
        self.b_seq.append((button, i))
      else:
        raise Exception("fag")
      i += 1
    self.o_seq.append((100000000000, len(seq)))
    self.b_seq.append((100000000000, len(seq)))
      
  def go(self):
    while self.comp != len(self.seq):
      self.step()
      #print 'b', self.b_loc, self.b_curr
      #print 'o', self.o_loc, self.o_curr
      #print 'comp', self.comp
      #print 'time', self.time
    print self.time


  def step(self):
    o_step = self.o_seq[self.o_curr]
    b_step = self.b_seq[self.b_curr]
    if o_step[1] == self.comp:
      #print 'o going'
      o_time_to_comp = abs(o_step[0] - self.o_loc) + 1
      b_time_to_go = abs(b_step[0] - self.b_loc)
      if o_time_to_comp >= b_time_to_go:
        self.b_loc = b_step[0]
      else:
        if b_step[0] > self.b_loc:
          self.b_loc += o_time_to_comp
        else:
          self.b_loc -= o_time_to_comp
      self.o_loc = o_step[0]
      self.o_curr += 1
      self.time += o_time_to_comp
    elif b_step[1] == self.comp:
      #print 'b going'
      b_time_to_comp = abs(b_step[0] - self.b_loc) + 1
      o_time_to_go = abs(o_step[0] - self.o_loc)
      if b_time_to_comp >= o_time_to_go:
        self.o_loc = o_step[0]
      else:
        if o_step[0] > self.o_loc:
          self.o_loc += b_time_to_comp
        else:
          self.o_loc -= b_time_to_comp
      self.b_loc = b_step[0]
      self.b_curr += 1
      self.time += b_time_to_comp
    else:
      raise Exception("dumbass")
    self.comp += 1

#r = RobState(sequence)
#r.go()

n = int(sys.stdin.readline())
for x in range(n):
  line = sys.stdin.readline()
  vars = line.strip().split(" ")
  length = int(vars[0])
  assert(len(vars) == length * 2 + 1)
  seq = []
  for i in range(length):
    robot = vars[1 + 2 * i]
    button = int(vars[2 + 2 * i])
    seq.append((robot, button))
  r = RobState(seq)
  print "Case #%d:" % (x + 1),
  r.go()
