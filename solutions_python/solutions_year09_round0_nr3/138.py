f = open('a.in', 'r')
n = int(f.readline())
s = '#welcome to code jam'
MOD = 10000
for tno in range(n):
  w = f.readline()
  A = [0] * len(s)
  A[0] = 1
  sol = 0
  for c in w[:-1]:
    for i in range(len(s) - 2, -1, -1):
      if s[i + 1] == c:
        if i + 2 == len(s):
          sol += A[i]
          sol %= MOD
        A[i + 1] += A[i]
        A[i + 1] %= MOD
  print 'Case #%d: %04d' % (tno + 1, sol)
