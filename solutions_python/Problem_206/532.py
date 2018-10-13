import io, os, sys

data = open(sys.argv[1]).readlines()
n = int(data[0].strip())

num = 1
count = 0
i = 0
while count < n:
  count += 1
  i += 1
  A = data[i].split(' ')
  k = int(A[1].strip())
  d = int(A[0].strip())
  T = []
  for j in range(k):
    i += 1
    p = long(data[i].split(' ')[0])
    s = long(data[i].split(' ')[1])
    T.append((d-p)*1.0/s)
  T.sort()
  mt = T[-1]
  print 'Case #' + str(num) + ': ' + str(d*1.0/mt)
  num += 1
