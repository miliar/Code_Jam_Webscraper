import fileinput

def lights_on(n, k):
  tmp = 0
  for i in xrange(n):
    tmp = (tmp << 1) | 1
  return tmp == k % (tmp + 1)

l = 0
for line in fileinput.input():
  i = 0
  acc = ""
  nbrs = []
  while line[i] != '\n':
    if line[i] == ' ':
      nbrs.append(int(acc))
      acc = ""
    acc += line[i]
    i += 1
  nbrs.append(int(acc))
  if len(nbrs) == 2:
    if lights_on(nbrs[0], nbrs[1]):
      print "Case #"+str(l)+": ON"
    else:
      print "Case #"+str(l)+": OFF"
  l += 1
