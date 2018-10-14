from math import sqrt, ceil, floor

# ============================================

def isPalindrome(n):
  s = str(n)
  sp = s[::-1]
  return (s==sp)

# ============================================

def solutions(A,B):
  
  result = []
  sqrtA = long(ceil(sqrt(float(A))))
  sqrtB = long(floor(sqrt(float(B))))
  for n in range(sqrtA,sqrtB+1):
    if isPalindrome(n) and isPalindrome(n*n):
      result.append(n*n)
  return result

# ============================================

f = open("C-large-1.in","r")
numTestCases = int(f.readline())

minA = None
maxB = None
for testCase in range(numTestCases):
  data = f.readline().strip().split()
  data = map(long,data)
  A = data[0]
  B = data[1]
  if (minA==None): minA = A
  elif (A<minA): minA = A
  if (maxB==None): maxB = B
  elif (B>maxB): maxB = B

palindromes = solutions(minA,maxB)

f.seek(0)
f.readline()
for testCase in range(numTestCases):

  data = f.readline().strip().split()
  data = map(long,data)
  A = data[0]
  B = data[1]

  count = 0
  for p in palindromes:
    if (p>=A and p<=B): count += 1

  print "Case #%i: %i" % (testCase+1, count)

f.close()


