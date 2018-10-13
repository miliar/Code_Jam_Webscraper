#
# Google CodeJam 2009
# Alien Languages
#
# Input
# 
# The first line of input contains 3 integers, L, D and N separated
# by a space. D lines follow, each containing one word of length L.
# These are the words that are known to exist in the alien language.
# N test cases then follow, each on its own line and each consisting
# of a pattern as described above. You may assume that all known words
# provided are unique.
# 
# Output
# 
# For each test case, output
# 
# Case #X: K
# 
# where X is the test case number, starting from 1, and K indicates
# how many words in the alien language match the pattern.
# 
# Limits
# 
# Small dataset
# 
# 1 <= L <= 10
# 1 <= D <= 25
# 1 <= N <= 10
# 
# Large dataset
# 
# 1 <= L <= 15
# 1 <= D <= 5000
# 1 <= N <= 500
# 
# Sample
#
# Input                     Output
#   3 5 4                   Case #1: 2
#   abc                     Case #2: 1
#   bca                     Case #3: 3
#   dac                     Case #4: 0
#   dbc
#   cba
#   (ab)(bc)(ca)
#   abc
#   (abc)(abc)(abc)
#   (zyx)bc

def loadFile(filename):
  """
    Load a file in the input format into a dictionary.

    retval['L'], retval['D'], retval['K'] as expected
    retval['dict'] = a tree building all dictionary words
    retval['casesIn'] = list of test cases (input)
  """

  retval = {}

  with open(filename, "rt") as file:
    firstLine = file.readline()

    parts = firstLine.split(' ')

    L = int(parts[0])
    D = int(parts[1])
    N = int(parts[2])

    retval['L'] = L
    retval['D'] = D
    retval['N'] = N

    dict = {}

    for i in range(D):
      word = file.readline()

      if word:
        word = word.strip(' \t\n')

        if word:
          curnode = dict

          for c in word:
            if not c in curnode.keys():
              curnode[c] = {}

            curnode = curnode[c]

    retval['dict'] = dict

    tests = []

    for i in range(N):
      test = file.readline()

      if test:
        test = test.strip(' \t\n')

        if test:
          tests.append(test)

    retval['casesIn'] = tests

  return retval

def countPossibilities(dictnode, testCase):
  """
    Count the possibilities in the test case.
  """

  if not testCase:
    return 1

  if testCase[0] != '(':
    if testCase[0] in dictnode.keys():
      return countPossibilities(dictnode[testCase[0]], testCase[1:])
    else:
      return 0
  else:
    i = testCase.find(')')
    part = testCase[0:i+1]
    rest = testCase[i+1:]
    part = part.strip('()')

    count = 0

    for c in part:
      if c in dictnode.keys():
        count = count + countPossibilities(dictnode[c], rest)
      else:
        continue

    return count

def process(data):
  """
    Run the tests on a data set.
  """

  i = 1

  for test in data['casesIn']:
    print "Case #%d: %d" % (i, countPossibilities(data['dict'], test))
    i = i + 1

#data = loadFile('alien_sample.in')

#data = loadFile('A-small-attempt0.in')
#data = loadFile('A-small-attempt1.in')
data = loadFile('A-large.in')

process(data)
