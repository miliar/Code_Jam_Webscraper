
t = input()
r = 0
while (r < t):
  n, s = raw_input().split()
  n = int(n) + 1
  c = 0
  o = 0
  for i in range(n):
    d = int(s[i])
    if d > 0 and o < i:
      c += i - o
      o += i - o
    o += d
  print 'Case #' + str(r + 1) + ':', str(c)
  r += 1
