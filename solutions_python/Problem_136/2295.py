# Qualification Round Problem B

i = open("B-large.in", "r")
o = open("B-large.out", "w")

T = int(i.readline())

for c in range(1, T + 1):
  CPS = 2.0
  C, F, X = map(float, i.readline().split(" "))

  cookies = 0
  time = 0

  while cookies < X:
    time1 = X/CPS
    time2 = C/CPS + X/(CPS + F)
    if time1 <= time2:
      cookies += X
      time += time1
    else:
      cookies = 0
      time += C/CPS
      CPS += F

  result = time

  o.write("Case #{0}: {1:1.7f}\n".format(c, result, X, cookies, X == cookies))

i.close()
o.close()