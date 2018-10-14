import math
'''
example:
N = 100
K = 10
1p -> {49, 50} : (49, 50)
2p -> {49, 24, 25}: (24, 25)
3p -> {24, 24, 24, 25}: (24, 24)
4p -> {24, 24, 24, 12, 12}: (12, 12)
5p -> {11, 12, 24, 24, 12, 12}: (11, 12)
6p -> {11, 12, 11, 12, 24, 12, 12}: (11, 12)
7p -> {11, 12, 11, 12, 11, 12, 12, 12}: (11, 12)
8p -> {11, 5, 6, 11, 12, 11, 12, 12, 12}: (5, 6)
9p -> {11, 5, 6, 11, 5, 6, 11, 12, 12, 12}: (5, 6)
'''


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t+1):
  N, K = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  # print N, K
  h = int(math.log(K, 2))
  # print h
  cost_people = int(math.pow(2, h) - 1)
  other_people = K - cost_people
  other_space = N - cost_people
  # print other_space
  # print math.pow(2, h)
  base = other_space / int(math.pow(2, h))
  # print base
  larger_number = int(other_space % int(math.pow(2, h)))
  # print other_people,larger_number
  small_number = int(math.pow(2, h) - other_space % math.pow(2, h))
  if other_people > larger_number:
    #   print float(base-1)/2
      MaxDistance = base/2
      SmallDistance = (base-1)/2
  else:
      MaxDistance = (base+1)/2
      SmallDistance = (base)/2


  print "Case #{}: {} {}".format(i, MaxDistance, SmallDistance)
  # check out .format's specification for more formatting options
