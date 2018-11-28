class A:
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
	#self.T = int(line[:-1])
      else:
	columns = line.split(' ')
	N = int(columns[0])
	bottons = []
	for j in xrange(N):
	  bottons.append((columns[1+2*j], int(columns[2+2*j])))
	inputs.append((N, bottons))
    #print i
    return inputs

  def solve(self, inputs):
    i = 1
    bots = ['O', 'B']
    result = []
    for N, seq in inputs:
      botstatus = dict()
      for bot in bots:
	botstatus[bot] = (1, 0)
      for target in seq:
	bot = target[0]
	timeElapsed = abs(target[1] - botstatus[bot][0]) + 1
	maxTimestamp = max([status[1] for status in botstatus.values()])
	newTimestamp = (botstatus[bot][1] + timeElapsed) if (botstatus[bot][1] + timeElapsed > maxTimestamp) else (maxTimestamp + 1)
	#print timeElapsed
	botstatus[bot] = (target[1], newTimestamp)
	#print botstatus
      result.append("Case #%d: %d" % (i, max([status[1] for status in botstatus.values()])))
      i += 1
    return result
	    
  def output(self, outputs):
    for line in outputs:
      print line
  
  def searchseq(self, bot, seq, start, end):
    for i in xrange(start + 1, end):
      if seq[i][0] == bot:
	return i
    return None

if __name__ == '__main__':
  A = A('A-small-attempt0.in')

