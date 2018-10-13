# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer

flip = lambda x: "+" if x == "-" else "-"
for i in xrange(1, t + 1):
  S, K = raw_input().split(" ")
  K = int(K)
  S = list(S)
  Slen = len(S)
  test = ["+"]*Slen
  count = 0
  flag = 0
  for outer in xrange(Slen, K-2, -1):
      if S == test:
          flag = 1
          break
      if S[outer-1] == "+":
          continue
      for j in xrange(outer, outer-K, -1):
         S[j-1] = flip(S[j-1])
      count+=1
  if flag:
      print "Case #{}: {}".format(i, count)
  else:
      print "Case #{}: {}".format(i, "IMPOSSIBLE")
  # check out .format's specification for more formatting options