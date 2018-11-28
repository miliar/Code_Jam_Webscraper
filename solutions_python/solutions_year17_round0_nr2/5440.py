def check_decreasing(n):
  n_list = [int(d) for d in str(n)]
  n_len = len(n_list)
  i = 0
  while i < n_len-1:
    if n_list[i] > n_list[i+1]:
      return False
    i = i+1
  return True

mapping = {}
for n in xrange(1,1001):
  x = n
  while x > 0:
    if check_decreasing(x):
      mapping[n] = x
      break
    x = x - 1


for i in xrange(1,1+input()):
  n = input()
  print "Case #%s: %s" % (i, mapping[n])