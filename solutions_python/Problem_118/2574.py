import math

def isPalindrome(n):
  s = str(n)
  left = s[:len(s)/2]
  right = s[len(s)/2 + (len(s)%2):]
  return left == right[::-1]

def countFS(start, end):
#  print "start: %d end: %d" % (start, end)
  isqrt = int(math.sqrt(start))
  isqr = int(isqrt**2)
  if (isqr < start):
#    print "bad start: moving up to the next"
    isqrt = isqrt + 1
    isqr = isqrt**2

#  print "isqrt = %d, isqr = %d" % (isqrt, isqr)
  cFS = 0

  while isqr <= end:
#    print "isqr = %d isqrt= %d" % (isqr, isqrt)
    if isPalindrome(isqrt) and isPalindrome(isqr):
#      print "\t%d is palindrome cFS = %d" % (isqr, cFS)
      cFS = cFS + 1
    isqr = isqr + 2*isqrt + 1
    isqrt = isqrt + 1

  return cFS

f = open('problem2', 'r')
results = []
nproblems = int(f.readline())
while nproblems > 0:

  [start, end] = f.readline().strip().split(' ')
  result = countFS(int(start), int(end))
  results.append('Case #%s: %s' % (len(results)+1, result))
#  print result
  nproblems = nproblems - 1

for result in results:
  print result
