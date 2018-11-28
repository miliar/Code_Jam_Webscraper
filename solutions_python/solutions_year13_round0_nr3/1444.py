f = open('input1.in')

numCases = int(f.readline())
cases = []

def isPalindrome(number):
  s = str(number)
  reverse = s[::-1]

  if s == reverse:
    return True
  return False

def findSquares(low, high):
  num = 0
  for i in range(1,101):
    square = i**2

    if square < low or square > high:
      continue

    if isPalindrome(square) and isPalindrome(i):
      num += 1

  return num



for i,line in enumerate(f):
  nums = line.split(' ')
  low = int(nums[0])
  high = int(nums[1])

  print 'Case #{0}: {1}'.format(i+1, findSquares(low, high))
