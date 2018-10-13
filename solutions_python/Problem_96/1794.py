

def getScores(sum):
  if sum % 3 == 0:
    first = sum / 3
    return [first, first, first]
  else:
    first = sum / 3
    third = first + 1
    second = sum - first - third
    return [first, second, third]


def testGetScore():
  for i in xrange(4, 1000):
    scores = getScrores(i)
    diff = max(scores) - min(scores)
    if (diff > 1):
      print i, scores


if __name__=="__main__":
  import sys
  f = sys.stdin
  T = int(f.readline().strip())
  for i in xrange(T):
    segs = [int(x) for x in f.readline().strip().split()]
    N = segs[0]
    S = segs[1]
    p = segs[2]
    sums = segs[3:3+N]
    count = 0
    for sum in sums:
      scores = getScores(sum)
      high = max(scores)
      low = min(scores)
      if high >= p:
        count += 1
      elif S > 0 and low > 0 and high + 1 >= p:
        S -= 1
        count +=1
    print "Case #%d: %d" % (i+1, count)