#fair and square

import math

def rdigits(n):
  while n > 9:
    yield n % 10
    n = n / 10
  yield n

def is_palindrome(n):
  digits = list(rdigits(n))
  while True:
    if len(digits) < 2:
      return True
    if digits[0] != digits[-1]:
      return False
    digits = digits[1:-1]

def find_fair_and_square(start, end):
  n = int(math.ceil(math.sqrt(start)))

  while n <= end:
    if not is_palindrome(n):
      n += 1
      continue
    nsquared = n * n
    if nsquared > end:
      return
    if is_palindrome(nsquared):
      yield nsquared
    n += 1

def main(filename):
  with open(filename, 'r') as inf:
    lines = inf.readlines()
  with open(filename + '.out', 'w') as outf:
    for i, line in enumerate(lines[1:]):
      start, end = map(int, line.strip().split())
      print >> outf, ("Case #%d: %d" % (i + 1,
        len(list(find_fair_and_square(start, end)))))
