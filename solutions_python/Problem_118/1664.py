import sys
import math

def gen_square_palindrome(x, y):
  # Generates square palindromes starting from x
  s = str(x)
  odd = len(s) % 2 == 1
  n = int(s[:(len(s)+1)/2])
  while True:
    s = str(n)
    if odd:
      s = s + s[::-1][1:]
      int_s = int(s)
      if is_square(int_s) and is_palindrome(int(math.sqrt(int_s))):
        yield int_s
      if int_s >= y:
        return
      n += 1
      if len(str(n)) > len(str(n-1)):
        odd = False
        n /= 10
    else:
      s = s + s[::-1]
      int_s = int(s)
      if is_square(int_s) and is_palindrome(int(math.sqrt(int_s))):
        yield int_s
      if int_s >= y:
        return
      n += 1
      if len(str(n)) > len(str(n-1)):
        odd = True

def is_palindrome(x):
  s = str(x)
  return s == s[::-1]

def is_square(x):
  sq = math.sqrt(x)
  return sq == int(sq)

if __name__ == "__main__":
  with open(sys.argv[1], 'r') as f:
    min_input = int(sys.argv[2])
    max_input = int(sys.argv[3])
    fair_squares = set(gen_square_palindrome(min_input, max_input))
    ncases = int(f.readline())
    for i in xrange(ncases):
      A,B = tuple(map(int, f.readline().split()))
      nfairsquare = len([x for x in fair_squares if x >= A and x <=B])
      print "Case #%d: %d" % (i+1, nfairsquare)

