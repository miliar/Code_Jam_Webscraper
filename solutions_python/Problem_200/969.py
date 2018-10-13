
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for k in xrange(1, t + 1):
  N = list(raw_input()) # read a list of integers, 2 in this case
  for i in range(len(N) - 1, 0, -1):
      if int(N[i]) < int(N[i - 1]):
          N[i - 1] = str(int(N[i - 1]) - 1)
          for j in range(i, len(N)):
              if N[j] == '9': break
              N[j] = '9'

  print "Case #{}: {}".format(k, int(''.join(N)))
  # check out .format's specification for more formatting options


