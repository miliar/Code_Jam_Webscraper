def isTidy(n):
  nArray = map(lambda d: int(d), str(n))
  for i in range(len(nArray) - 1):
    if nArray[i] > nArray[i + 1]:
      return False
  return True

"""
def findTidy(n):
  curr = n
  while not isTidy(curr):
    curr -= 1
  return curr
"""

def findTidy(n):
  curr = n
  pos = 1
  while not isTidy(curr):
    digit = int(str(curr)[-pos])
    if digit != 9:
      curr -= (digit + 1) * 10 ** (pos - 1)
    pos += 1
  return curr

if __name__ == '__main__':
  noTestCases = int(raw_input())
  for testCaseNo in range(1, noTestCases + 1):
    n = int(raw_input())
    prevTidy = findTidy(n)
    print 'Case #' + str(testCaseNo) + ': ' + str(prevTidy)