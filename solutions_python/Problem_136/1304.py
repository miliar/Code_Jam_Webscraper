def line(f):
  return f.readline().strip()

i = open("B-large.in", "r")
o = open("1.out", "w")

T = int(line(i))

def solve(c, f, x):
  time = 0
  cookies = 0
  speed = 2
  while cookies < x:
    if cookies < c:
      time += (min(x, c) - cookies) / speed
      cookies = min(x, c)
    else:
      t1 = (x - cookies) / speed
      t2 = (x - cookies + c) / (speed + f)
      if t1 < t2:
        time += t1
        cookies = x
      else:
        cookies -= c
        speed += f
  return time

for t in xrange(T):
  c, f, x = map(float, line(i).split())
  time = solve(c, f, x)
  print>>o, "Case #%d: %.7f" % (t+1, time)
