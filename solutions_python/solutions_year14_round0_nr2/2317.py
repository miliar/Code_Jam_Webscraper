t = int(raw_input())

for i in range(t):
  s = raw_input()
  s = s.split()

  c = float(s[0])
  f = float(s[1])
  x = float(s[2])

  r = 2.0

  z = 0.0

  a = x/r
  b = c/r + x/(r+f)

  while a > b:
    z = z + c/r
    r = r + f
    a = x/r
    b = c/r + x/(r+f)

  z = z + x/r

  print "Case #%d: %.7f"%(i+1, z)
