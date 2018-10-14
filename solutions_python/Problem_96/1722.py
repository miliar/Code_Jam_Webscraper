import sys

class Usage(Exception):
  def __init__(self, msg):
    self.msg = msg

def main(argv=None):

  nJudges = 3

  try:
    filename = 'data.txt'
    file = open(filename, 'r')
    nTestCases = int(file.readline().rstrip())

    outfile = open('answer.txt', 'w')

    for i in xrange(nTestCases):
      params = file.readline().rstrip().split(' ')
      nGooglers = int(params[0])
      nSurprisingTriplets = int(params[1])
      p = int(params[2])
      scores = params[3:]
      nTotal = 0
      nQualify = 0
      nSurprising = 0
      nBoth = 0
      for s in scores:
        v = int(s)
        d = v / nJudges
        m = v % nJudges
        if d == 0 and m == 0 and p > 0:
          continue
        elif m == 0 and d+1 >= p and d >= p:
          nBoth += 1
        elif m == 0 and d+1 >= p:
          nSurprising += 1
        elif m == 2 and d+m >= p and d+1 >= p:
          nBoth += 1
        elif m == 2 and d+m >= p:
          nSurprising += 1
        elif m == 1 and d+1 >= p:
          nQualify += 1
      if nSurprising >= nSurprisingTriplets:
        nTotal += nSurprisingTriplets
      else:
        nTotal += nSurprising
      nTotal += nQualify + nBoth
      outfile.write('Case #{0}: {1}\n'.format(i+1, nTotal))
  except:
    print sys.stderr
    return 2

if __name__ == "__main__":
    sys.exit(main())

