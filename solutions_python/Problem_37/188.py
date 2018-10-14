unhappy = { 2: set([0]), 3: set([0]), 4: set([0]), 5: set([0]), 6: set([0]), 7: set([0]), 8: set([0]), 9: set([0]), 10: set([0]) }
happy = { 2: set([1]), 3: set([1]), 4: set([1]), 5: set([1]), 6: set([1]), 7: set([1]), 8: set([1]), 9: set([1]), 10: set([1]) }

def buildNumberInBase(n, b):
  """
    Return a list of digits of the number n in base b.

    Such that sum( digit[i] * b^i ) = n

    (123, 10) -> [3, 2, 1]
    (10, 2) -> [0, 1, 0, 1]
  """
  
#  global digits

  if n == 0:
    return [0]

#  if not b in digits.keys():
#    digits[b] = {}

#  if n in digits[b]:
#    return digits[b][n]

  orig = n
  i = 1
  retval = []

  while n > 0:
    nexti = i * b
    d = n % nexti

    retval.append(d / i)

    n = n - d
    i = nexti

#  digits[b][orig] = retval
  return retval

def happystep(n, b):
  """
    Run the happy step on a number and return the new number.
  """

  d = buildNumberInBase(n, b)

  squared = [ i * i for i in d ]

  return sum(squared)

def isHappy(n, b):
  """
    Run the happy algorithm.
  """

  global unhappy
  global happy

#  if not b in unhappy.keys():
#    unhappy[b] = set([0])

#  if not b in happy.keys():
#    happy[b] = set([1])

  uh = unhappy[b]
  h = happy[b]

  chain = []

  while True:
#    print chain
    if n in uh:
      # All elements in chain are bad
      uh = uh.union(chain)

      return False
    elif n in h:
      # All elements in chain are good
      h = h.union(chain)

      return True
    elif n in chain:
      # Loops are bad
      uh = uh.union(chain)

      return False
    else:
      # Add to chain
      chain.append(n)

      # Get next number
      n = happystep(n, b)

def findSmallestHappyNumber(bases):
  """
    Find the smallest number that's happy in all provided bases.
  """

  global happy, unhappy, digits

  # See if there is a common happy number in all bases
  s = None
  useS = True
  smallestBiggest = None

  for b in bases:
    if s:
      s = s.intersection(happy[b] - set([1]))
    else:
      s = happy[b] - set([1])

    if smallestBiggest:
      m = max(happy[b])
      if m < smallestBiggest:
        smallestBiggest = m
    else:
      smallestBiggest = max(happy[b])

  if useS and s and (len(s) > 1):
    return min(s)

  if useS and (smallestBiggest > 1):
    n = smallestBiggest
  else:
    n = 2

  while True:
#    print "Testing %d" % (n, )
    ishappy = True

    for b in bases:
      if not isHappy(n, b):
#        print "--> %d not happy in %d" % (n, b)
        ishappy = False
        break

    if ishappy:
      return n
    else:
      n = n + 1

def process(filename):
  """
    Read datafile.
  """

  retval = {}

  with open(filename, "rt") as file:
    T = int(file.readline())

    for i in range(T):
      bases = [ int(x) for x in file.readline().strip().split() ]

      print "Case #%d: %d" % (i + 1, findSmallestHappyNumber(bases))

#print isHappy(26, 2)
#print isHappy(26, 3)
#print isHappy(26, 7)
#print isHappy(82, 10)
#print isHappy(2, 3)
#print isHappy(3, 9)

#print findSmallestHappyNumber([3])
#print findSmallestHappyNumber([2,3])
#print findSmallestHappyNumber([2,3,7])
#print findSmallestHappyNumber([9,10])

#process('happy-sample.in')
#import cProfile
#cProfile.run('process("A-small-attempt0.in")')
process("A-small-attempt1.in")
