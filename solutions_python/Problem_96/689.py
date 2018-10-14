import sys

fin = open('in.txt', 'r')
fout = open('out.txt', 'w')

n = int(fin.readline())
for t in xrange(0, n):
  array = [int(x) for x in  fin.readline().split()]
  k = array[0]
  s = array[1]
  p = array[2]
  ma = max(3*p - 2,0)
  mi = max(3*p - 4,2)
  count = 0
  for j in xrange(0, k):
    cur = array[j + 3]
    if cur >= ma:
      count+=1
    else:
      if cur >= mi:
        if s > 0:
          s -= 1
          count += 1
  fout.write("Case #" + str(t + 1) + ": " + str(count) + "\n")
