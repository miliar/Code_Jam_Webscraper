import sys

class C:
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
	pass
      else:
	columns = line.split(' ')
	numbers = map(lambda x: int(x), columns)
	inputs.append(numbers)
    return inputs

  def solve(self, inputs):
    i = 1
    result = []
    for numbers in inputs:
      if reduce(lambda x,y: x ^ y, numbers, 0) != 0:
	result.append("Case #%d: NO" % i)
      else:
	result.append("Case #%d: %d" % (i, sum(numbers) - min(numbers)))
      i += 1
    return result
	    
  def output(self, outputs):
    for line in outputs:
      print line

if __name__ == '__main__':
  C = C(sys.argv[1])

