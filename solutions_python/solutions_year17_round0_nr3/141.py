# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def bathroom_stall(N, K):
  if K == 1:
    return (N / 2, (N - 1) / 2)

  if N % 2 == 0 and K % 2 == 0:
    return bathroom_stall(N / 2, K / 2)
  if N % 2 == 0 and K % 2 == 1:
    return bathroom_stall(N / 2 - 1, K / 2)
  if N % 2 == 1 and K % 2 == 0:
    return bathroom_stall(N / 2, K / 2)
  if N % 2 == 1 and K % 2 == 1:
    return bathroom_stall(N / 2, K / 2)


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
 N, K = [int(s) for s in raw_input().split(" ")]  
 max_LR, min_LR = bathroom_stall(N, K)
 print "Case #{}: {} {}".format(i, max_LR, min_LR)
 # check out .format's specification for more formatting options