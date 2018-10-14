import time
import cProfile
import operator
import sys


def is_palindrome(n):
  return n == n[::-1]


def palindromes_raw(limit):
  for n in range(0, limit):
    yield str(n)

  for n in range(0, limit):
    yield "%d%d" % (n, n)

  for p in palindromes_raw(limit):
    for n in range(0, limit):
      yield "%s%s%s" % (n, p, n)


def palindromes(limit=10):
  for p in palindromes_raw(limit):
    if p[0] == '0':
      continue
    yield p


def palindromes_with_two(start, end):
  pals = []
  for i in range(start, end):
    if i % 2 == 0:
      pals.append("2%s2" % ("0" * (i-2)))
    else:
      pals.append("2%s2" % ("0" * (i-2)))
      pals.append("2%s1%s2" % ("0" * ((i-3) / 2), "0" * ((i-3) / 2)))

      pals.append("1%s2%s1" % ("0" * ((i-3) / 2), "0" * ((i-3) / 2)))
      for j in range(i/2 - 1):
        half = "1%s1%s" % ("0" * ((i/2) - j - 2), "0" * j)
        pals.append((half + "2" + half[::-1]))
  return pals


"""
start = time.time()
pals = [n for n in range(1, 10000000) if is_palindrome(str(n))]
#print pals
print len(pals)
print time.time() - start"""


def find_fair_square():
  start = time.time()
  gen_pals = []
  mapping = {2: 4, 3: 9}
  gen = palindromes(2)
  while True:
    p = int(gen.next())
    if p > 10**50:
      break
    sqr = p*p
    if is_palindrome(str(sqr)):
      #print sqr
      gen_pals.append(sqr)
      mapping[p] = sqr

  for pal in palindromes_with_two(2, 51):
    p = int(pal)
    sqr = p*p
    if is_palindrome(str(sqr)):
      #print sqr
      gen_pals.append(sqr)
      mapping[p] = sqr

  #print gen_pals
  #print len(gen_pals)
  #print time.time() - start
  mapping = sorted(mapping.iteritems(), key=operator.itemgetter(1))
  for a, b in mapping:
    #print "%d: %d" % (a, b)
    print b
    pass
  return gen_pals


def binary_search(x, xs, low, high):
  if low >= high:
    return high

  median = (low + high) / 2
  if x > xs[median]:
    return binary_search(x, xs, median+1, high)
  if x < xs[median]:
    return binary_search(x, xs, low, median-1)
  else:
    return median


def read_pals(filename):
  pals = []
  with open(filename) as f:
    for line in f:
      pals.append(int(line))
  return pals


def solve_input():
  #pals = sorted(find_fair_square())
  pals = read_pals("02_pals")
  num_cases = int(sys.stdin.readline())
  for i in range(num_cases):
    print "Case #%d:" % (i + 1),

    a, b = sys.stdin.readline().strip().split(" ")
    a, b = int(a), int(b)

    a_i = binary_search(a, pals, 0, len(pals))
    b_i = binary_search(b, pals, 0, len(pals))

    count = b_i - a_i
    if(pals[a_i] > a and pals[a_i] <= b):
      count += 1

    pal_interval = [p for p in pals if p >= a and p <= b]
    #print "%d <= x <= %d -- %d:%d -- %d - %d" % (a, b, a_i, b_i, count, len(pal_interval))
    print "%d" % len(pal_interval)


#find_fair_square()
solve_input()



#cProfile.run('find_fair_square()')
