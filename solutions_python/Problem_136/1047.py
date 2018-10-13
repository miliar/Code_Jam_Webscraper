f = open('cookie_clicker_data.txt')
T = int(f.readline())
for turn in range(T):
  C, F, X = [float(x) for x in f.readline().split()]
  r = 2
  time = 0
  while (X - C)/r > X / (r + F):
    time += C / r
    r += F
  time += X / r
  print "Case #" + str(turn+1) + ":", time