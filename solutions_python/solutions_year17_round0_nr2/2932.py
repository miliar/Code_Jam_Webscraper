from os import sys

def digit(N, i):
  N0 = N
  i0 = i
  while i > 0:
    N /= 10
    i -= 1
  return N % 10

def solve(N):
  i = 18
  output = []
  index_of_first_repeat = None
  while i >= 0:
    if i == 0:
      output.append(digit(N, i))
      break
    A = digit(N, i)
    B = digit(N, i-1)
    if A > B:
      output.append(digit(N, i) - 1)
      output += [9]*i
      break
    else:
      output.append(digit(N, i))
      if A == B and index_of_first_repeat == None:
        index_of_first_repeat = N
    i -= 1

  i = 17
  while i > 0:
    if output[i] < output[i-1]:
      output[i] = 9
      output[i-1] -= 1
    i -= 1

  return int("".join([str(d) for d in output]))

num_cases = int(sys.stdin.readline())

for case in range(1,num_cases+1):
  N = int(sys.stdin.readline())
  print "Case #" + str(case) + ":", solve(N)
