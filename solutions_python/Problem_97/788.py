import sys

f = open(sys.argv[1])

N = int(f.readline()[:-1])
sets = []
for i in xrange(N):
  line = f.readline()[:-1]
  p_line = line.split(' ')
  sets.append((int(p_line[0]), int(p_line[1])))



case = 1

for (A,B) in sets:
  dic = {}
  for n in xrange(A, B+1):
    s = str(n)
    for k in xrange(len(s)):
      m = int(s[len(s)-k:] + s[:len(s)-k])
      if A <= n and n < m and m <= B: dic[(n,m)] = 0
  print 'Case #%d: %d' % (case, len(dic))
  case += 1


