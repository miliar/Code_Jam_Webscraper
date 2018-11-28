import math

def isPalindrome(num):
  if len(num) <= 0:
    return True
  if (num[0] == num[len(num)-1]):
    return isPalindrome(num[1:-1])
  else:
    return False

def isSquare(num):
  value = math.sqrt(num)
  if value - math.floor(value) == 0:
    return True
  return False

answers = set()

def isFairSquare(num):
  return num in answers or (isPalindrome(str(num)) and isSquare(num) and isPalindrome(str(int(math.sqrt(num)))))

times = int(raw_input())

for time in xrange(times):
  count = 0
  A, B = map(int, raw_input().split())
  for i in xrange(A,B+1):
    if isFairSquare(i):
      answers.add(i)
      count += 1
  print "Case #%d: %d" % (time+1, count)
