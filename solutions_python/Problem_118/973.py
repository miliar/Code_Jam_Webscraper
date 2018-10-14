import sys, math

def isPal(num):
  s = str(num)
  for i in xrange(len(s)/2):
    if s[i] != s[len(s)-1-i]:
      return False
  return True

def findClosestRoot(num):
  sq = math.sqrt(A)
  return int(math.ceil(sq))

if __name__ == "__main__":
  lines = sys.stdin.readlines()
  for i in range(1, len(lines)):
    line = lines[i].strip().split(' ')
    A = int(line[0])
    B = int(line[1])
    root = findClosestRoot(A)
    count = 0
    j = root * root
    while j <= B:
      if isPal(j) and isPal(root):
        count += 1
      root += 1
      j = root * root

    print "Case #{}: {}".format(i, count)

