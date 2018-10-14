




readfile = open("A-large.in")
writefile = open("output2.txt", "w")

lines = readfile.readlines()
assert int(lines[0]) == len(lines) - 1

for prob_num in xrange(1,len(lines)):
  line = lines[prob_num]
  seq, k = line.split()
  k = int(k)
  array = []
  for x in seq:
    assert(x in ['+','-'])
    if x == '+':
      array.append(0)
    elif x == '-':
      array.append(1)
  #solve
  # logic: all flips are time independent, just work from left to right
  count = 0
  while 1 in array:
    count += 1
    i = array.index(1)
    if i > len(array)-k:
      break
    for j in xrange(i,i+k):
      array[j] ^= 1
  if 1 in array:
    writefile.write("Case #%d: IMPOSSIBLE\n" % prob_num)
  else:
    writefile.write("Case #%d: %d\n" % (prob_num, count))

writefile.close()