#
# Google CodeJam 2009
# Welcome to Code Jam
#
#
# Problem
# 
# So you've registered. We sent you a welcoming email, to welcome you to
# code jam. But it's possible that you still don't feel welcomed to code
# jam. That's why we decided to name a problem "welcome to code jam." After
# solving this problem, we hope that you'll feel very welcome. Very
# welcome, that is, to code jam.
# 
# If you read the previous paragraph, you're probably wondering why it's
# there. But if you read it very carefully, you might notice that we have
# written the words "welcome to code jam" several times: 400263727 times
# in total. After all, it's easy to look through the paragraph and find
# a 'w'; then find an 'e' later in the paragraph; then find an 'l' after
# that, and so on. Your task is to write a program that can take any text
# and print out how many times that text contains the phrase "welcome to
# code jam".
# 
# To be more precise, given a text string, you are to determine how many
# times the string "welcome to code jam" appears as a sub-sequence of that
# string. In other words, find a sequence s of increasing indices into the
# input string such that the concatenation of input[s[0]], input[s[1]], 
# ..., input[s[18]] is the string "welcome to code jam".
# 
# The result of your calculation might be huge, so for convenience we would
# only like you to find the last 4 digits.
# 
# Input
# 
# The first line of input gives the number of test cases, N. The next N
# lines of input contain one test case each. Each test case is a single
# line of text, containing only lower-case letters and spaces. No line
# will start with a space, and no line will end with a space.
# 
# Output
# 
# For each test case, "Case #x: dddd", where x is the case number, and
# dddd is the last four digits of the answer. If the answer has fewer
# than 4 digits, please add zeroes at the front of your answer to make it
# exactly 4 digits long.
# 
# Limits
# 1 = N = 100
# 
# Small dataset
# Each line will be no longer than 30 characters.
# 
# Large dataset
# Each line will be no longer than 500 characters.
# 
# Sample
#
# Input
#
# 3
# elcomew elcome to code jam
# wweellccoommee to code qps jam
# welcome to codejam
# 
# Output
#
# Case #1: 0001
# Case #2: 0256
# Case #3: 0000
# 

def readFile(filename):
  """
    Read the file.
  """

  retval = []

  with open(filename, "rt") as file:
    firstLine = file.readline()
    firstLine = firstLine.strip(' \t\n')
    N = int(firstLine)

    for i in range(N):
      line = file.readline()
      line = line.strip(' \t\n')
      if line:
        retval.append(line)

  return retval

def countWelcomes(string):
  """
    Count number of times 'welcome to code jam' can
    be generated as defined in the problem.
  """

  count = 0

  # Our target string
  target = 'welcome to code jam'
  targetindex = 0

  # Start
  start = string.find('w')
  index = start

  # Found string indicies
  s = [-1 for i in range(len(target))]

  while start < len(string):
    t = string.find(target[targetindex], index)

    if t < 0:
      # not found

      if targetindex == 0:
        # Can't find any more
        break
      else:
        # back up one character
        s[targetindex] = 0
        index = s[targetindex-1] + 1
        targetindex = targetindex - 1
    else:
      # save index
      s[targetindex] = t
      index = t + 1

      # move to the next char
      targetindex = targetindex + 1

      if targetindex >= len(target):
        # no more chars, found one instance of the target
        count = count + 1

        # try looking for the same char again
        targetindex = targetindex - 1
        s[targetindex] = -1
        index = t + 1

  return count

def process(data):
  """
    Run the test.
  """

  i = 1
  for s in data:
    c = countWelcomes(s)

    print "Case #%d: %04d" % (i, c % 10000)
    i = i +1

#data = readFile('welcome-sample.in')
data = readFile('C-small-attempt0.in')
#data = readFile('C-large.in')
process(data)
