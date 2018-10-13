class Wizzard:
  def __init__(self):
    self.list = []
    self.base_elements = 'QWERASDF'
    # each element is 'ABC' where 'AB', 'BA' combine to 'C'
    self.combinations = []
    # each element is 'AB' where 'A', 'B' are opposed
    self.oppositions = []
  
  def add_combination(self, s):
    self.combinations.append(s)
  
  def add_opposition(self, s):
    self.oppositions.append(s)
  
  def combine(self):
    if len(self.list) < 2:
      return False
    top1 = self.list[-2] + self.list[-1]
    top2 = self.list[-1] + self.list[-2]
    for comb in self.combinations:
      if comb.startswith(top1) or comb.startswith(top2):
        del self.list[-1]
        self.list[-1] = comb[2]
        return True
    return False
  
  def is_opposed(self, c):
    for o in self.oppositions:
      if c == o[0] and o[1] in self.list:
        return True
      if c == o[1] and o[0] in self.list:
        return True
    return False
        
  def invoke(self, c):
    self.list.append(c)
    was_combined = False
    while self.combine():
      was_combined = True
    if not was_combined and self.is_opposed(c):
      self.list = []
  
  def format(self):
    return '[' + ', '.join(self.list) + ']'

def testcase(t):
  data = raw_input().split()
  i = 0
  w = Wizzard()
  C = int(data[i])
  i += 1
  for j in xrange(C):
    w.add_combination(data[i])
    i += 1
  D = int(data[i])
  i += 1
  for j in xrange(D):
    w.add_opposition(data[i])
    i += 1
  N = int(data[i])
  i += 1
  s = data[i]
  for j in xrange(N):
    w.invoke(s[j])
  print 'Case #%d: %s' % (t, w.format())

T = int(raw_input())
for i in xrange(T):
  testcase(i + 1)