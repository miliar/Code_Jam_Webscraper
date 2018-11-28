import sys
import math

T = int(sys.stdin.readline().strip())

found = set()

def next_palindrome(num):
  length=len(str(num))
  oddDigits=(length%2!=0)
  leftHalf=getLeftHalf(num)
  middle=getMiddle(num)
  if oddDigits:
      increment=pow(10, length/2)
      newNum=int(leftHalf+middle+leftHalf[::-1])
  else:
      increment=int(1.1*pow(10, length/2))
      newNum=int(leftHalf+leftHalf[::-1])
  if newNum>num:
      return newNum
  if middle!='9':
      return newNum+increment
  else:
      return next_palindrome(roundUp(num))
 
def getLeftHalf(num):
  return str(num)[:len(str(num))/2]
 
def getMiddle(num):
  return str(num)[(len(str(num))-1)/2]
 
def roundUp(num):
  length=len(str(num))
  increment=pow(10,((length/2)+1))
  return ((num/increment)+1)*increment

def is_palindrome(n):
  n = str(n)
  f = n[:int(math.ceil(len(n) / 2.0))]
  e = n[int(math.floor(len(n)/2.0)):][::-1]
  return f == e

def is_square(n):
  if n == 1:
    return True
  x = n // 2
  seen = set([x])
  while x * x != n:
    x = (x + (n // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

def is_both(n):
  return is_square(n) and is_palindrome(n)

def is_all(n):
  pal = is_palindrome(n)
  if not pal:
    return False
  sq = n ** 2
  return is_palindrome(sq)

def set_found(mini, maxi):
  a = int(math.ceil(math.sqrt(mini)))
  b = int(math.floor(math.sqrt(maxi)))
  i = a-1
  while i <= b:
    p = int(next_palindrome(i))
    if p <= b and is_all(p):
      found.update([p**2])
    i = p

set_found(1, 10 ** 15)

# def set_found2(maxi):
#   a = '1'
#   b = str(int(math.floor(math.sqrt(maxi))))
#   while len(a) <= len(b):
#     p = next_palindrome2(a)
#     if p <= b and is_all(p):
#       found.update([p**2])
#     a = p

# set_found2(10 ** 100)

for t in range(0,T):
  A, B = map(int, sys.stdin.readline().strip().split(" "))
  #print A, B
  # get the sqrt of A and B and use this as the range
  a = int(math.ceil(math.sqrt(A)))
  b = int(math.floor(math.sqrt(B)))
  def run():
    nums = filter(lambda n: n >= A and n <= B, list(found))
    #nums = filter(lambda n: n ** 2 >= A and n ** 2 <= B, nums) # sanity check
    return len(nums)

  ans = run()

  print "Case #%d: %s" % (t + 1, ans)

