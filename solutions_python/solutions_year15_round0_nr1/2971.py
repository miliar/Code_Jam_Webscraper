T = int(raw_input())

for each_testcase in range(T):
  smax, si = raw_input().split()
  si = map(lambda x: int(x), list(si))
  smax = int(smax)
  count = 0
  for i in range(smax+1):
    if sum(si[0:i]) < i:
      count += 1
      si[i] += 1
  print "Case #%d: %d" % (each_testcase+1, count)
