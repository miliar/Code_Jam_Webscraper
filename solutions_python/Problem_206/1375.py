def getTimeToDest(d, k, s):
  return (d - k) / float(s)

def getSpeedToDest(d, t):
  return d / float(t)

if __name__ == '__main__':
  noTestCases = int(raw_input())
  for testCaseNo in range(1, noTestCases + 1):
    d, n = map(int, raw_input().strip().split(' '))
    maxTimeToDest = 0
    for hi in range(n):
      k, s = map(int, raw_input().strip().split(' '))
      timeToDest = getTimeToDest(d, k, s)
      if timeToDest > maxTimeToDest:
        maxTimeToDest = timeToDest
    speedToDest = getSpeedToDest(d, maxTimeToDest)
    print 'Case #' + str(testCaseNo) + ': ' + '{0:.6f}'.format(speedToDest)