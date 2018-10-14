import sys

test_cases = int(sys.stdin.readline().strip())

for test_case in range(test_cases):
  A, B, K = [int(i) for i in sys.stdin.readline().strip().split(" ")]

  total_ways = 0
  for i in range(A):
    for j in range(B):
      if i&j < K:
        total_ways += 1
  print "Case #{0}: {1}".format(test_case+1, total_ways)
