
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t+1):
  N = raw_input()  # read a list of integers, 2 in this case
  N = list([int(n) for n in N])
  # print N
  # while 0 in N[1:]:
  #     tmp = N.index(0)
  #     N[tmp-1] = N[tmp-1]-1
  #
  #     for j in range(tmp, len(N)):
  #       #   print j
  #       #   print N.index(0)
  #         N[j] = 9
  #   #   print N
  #     result = int("".join([str(n) for n in N]))

  checked = False
  # print N
  while not checked:
      checked = True
      for j in range(len(N)-1):
          if N[j] > N[j+1]:
              checked = False
              N[j] = N[j] - 1
              for k in range(j+1, len(N)):
                 N[k] = 9
  result = int("".join([str(n) for n in N]))




  print "Case #{}: {}".format(i, result)
  # check out .format's specification for more formatting options
