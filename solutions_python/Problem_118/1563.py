import sys
import math


def palindrome(x):
  if str(x) == str(x)[::-1]:
    return True
  return False


def fair_square(a, b):
  res = []
  low = int(math.ceil(math.sqrt(a)))
  high = int(math.sqrt(b))
  res = []
  for i in xrange(low, high + 1):
    if not palindrome(i):
      continue
    elif not palindrome(i**2):
      continue
    res.append(i**2)
  return res

    


def main(fname):
  fin = open(fname)
  cases = int(fin.readline().strip())
  fair_squar = fair_square(1, 10 ** 14)

  for i in xrange(cases):
    a, b = fin.readline().split()
    a, b = int(a), int(b)
    count = 0
    for num in fair_squar:
      if a <= num <= b:
        count += 1

    print 'Case #%d: %d' % (i + 1, count)

if __name__ == '__main__':
  main(sys.argv[1])


