import math

def getSplitByEmptiness(n):
  leftOvers = n - 1
  half = leftOvers / 2
  isOdd = (leftOvers % 2) == 1
  return half + (1 if isOdd else 0), half

def getTier(n):
  return int(math.floor(math.log(n, 2)))

def findSplit(n, k):
  tier = getTier(k)
  emptySeatsForTier = n - ((2 ** tier) - 1)
  minSeatsPerPersonInTier = emptySeatsForTier / (2 ** tier)
  extraSeats = emptySeatsForTier % (2 ** tier)
  extraSeatForK = (k % (2 ** tier)) < extraSeats
  seatsForK = minSeatsPerPersonInTier + (1 if extraSeatForK else 0)
  #print tier, emptySeatsForTier, minSeatsPerPersonInTier, extraSeats, extraSeatForK, seatsForK
  return getSplitByEmptiness(seatsForK)

if __name__ == '__main__':
  noTestCases = int(raw_input())
  for testCaseNo in range(1, noTestCases + 1):
    n, k = map(int, raw_input().split(' '))
    hi, lo = findSplit(n, k)
    print 'Case #' + str(testCaseNo) + ': ' + str(hi) + ' ' + str(lo)