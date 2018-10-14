import math

def isPalindrome(n):
  strn = str(n)
  return strn == strn[::-1]

def isSquare(n):
  if n <= 0:
    return False
  sqrtn = math.sqrt(n)
  return sqrtn - int(sqrtn) == 0

def run(filename):
  f = open(filename)
  T = int(f.readline().strip())

  for test in range(T):
    fairAndSquare = 0
    print 'Case #{0}:'.format(str(test + 1)),
    testSpec = f.readline().strip().split();
    min = int(testSpec[0])
    max = int(testSpec[1])
    for n in range(min, max + 1):
      if isPalindrome(n) and isSquare(n) and isPalindrome(int(math.sqrt(n))):
         fairAndSquare += 1
    print fairAndSquare

if __name__ == '__main__':
  run('C-small-attempt0.in')

