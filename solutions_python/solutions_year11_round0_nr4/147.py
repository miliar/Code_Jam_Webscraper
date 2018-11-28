import sys

class D:
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
      elif i % 2 == 0:
	N = int(line[:-1])
      else:
	columns = line[:-1].split(' ')
	total = 0
	for j in xrange(N):
	  if j + 1 != int(columns[j]):
	    total += 1
	inputs.append(total)
    return inputs

  def solve(self, inputs):
    i = 1
    result = []
    for total in inputs:
      expectSwap = (total + 1) / 2
      result.append("Case #%d: %d" % (i, expectSwap * 2))
      i += 1
    return result
	    
  def output(self, outputs):
    for line in outputs:
      print line

if __name__ == '__main__':
  D = D(sys.argv[1])
