import sys

class magika:
  def __init__(self, combine, oppose):
    self.combine = combine
    self.oppose = oppose
    self.stack = []

  def newElement(self, element):
    if len(self.stack) == 0:
      self.stack.append(element)
      return
    if (element, self.stack[-1]) in self.combine:
      last = self.stack.pop()
      self.newElement(self.combine[(element, last)])
      return
    if element in self.oppose:
      #print "oppose:%s" % self.oppose[element]
      #print "stack:%s" % set(self.stack)
      #print "len:%d" % len(self.oppose[element] & set(self.stack))
      if len(self.oppose[element] & set(self.stack)) != 0:
	self.stack = []
	return
    self.stack.append(element)
    return

class B:
  def __init__(self, filename):
    inputs = self.parseInput(filename)
    outputs = self.solve(inputs)
    self.output(outputs)

  def parseInput(self, filename):
    f = file(filename)
    i = 0
    inputs = []
    for line in f:
      i += 1
      if i == 1:
	pass
      else:
	columns = line.split(' ')
	ptr = 0
	C = int(columns[ptr])
	ptr += 1
	combine = dict()
	for j in xrange(C):
	  combine[(columns[ptr][0], columns[ptr][1])] = columns[ptr][2]
	  combine[(columns[ptr][1], columns[ptr][0])] = columns[ptr][2]
	  ptr += 1
	D = int(columns[ptr])
	ptr += 1
	oppose = dict()
	for j in xrange(D):
	  first = columns[ptr][0]
	  second = columns[ptr][1]
	  if first not in oppose:
	    oppose[first] = set()
	  if second not in oppose:
	    oppose[second] = set()
	  oppose[first].add(second)
	  oppose[second].add(first)
	  ptr += 1
	seq = columns[ptr + 1][:-1]
	inputs.append((combine, oppose, seq))
    return inputs

  def solve(self, inputs):
    i = 1
    result = []
    for combine, oppose, seq in inputs:
      magi = magika(combine, oppose)
      for c in seq:
	magi.newElement(c)
      try:
	result.append("Case #%d: [%s]" % (i, reduce(lambda x, y: "%s, %s" % (x, y), magi.stack[1:], magi.stack[0])))
      except:
	result.append("Case #%d: []" % i)
      i += 1
    return result
	    
  def output(self, outputs):
    for line in outputs:
      print line

if __name__ == '__main__':
  B = B(sys.argv[1])

