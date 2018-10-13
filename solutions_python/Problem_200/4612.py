# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n = int(raw_input())  # read a list of integers
  strN = str(n)
  tempStr = strN

  def isNonDec(num):
      for i in range(1, len(num)):
          if int(num[i-1]) > int(num[i]): return False
      return True

  while not isNonDec(tempStr):
      tempStr = str(int(tempStr) - 1)

  print "Case #{}: {}".format(i, tempStr)
