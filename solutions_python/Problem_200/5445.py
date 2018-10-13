t = int(raw_input())  # read a line with a single integer


def is_tidy(N):
  tidy = True
  for j in range(len(str(N))-1):
    p = int(str(N)[j])
    c = int(str(N)[j+1])
    if c < p:
      tidy = False
      break
    else:
      tidy = True
  return tidy

for i in xrange(1, t + 1):
  N = int(raw_input())
  while not is_tidy(N):
    N = N - 1
  Y = N
  print "Case #{}: {} ".format(i, Y)
