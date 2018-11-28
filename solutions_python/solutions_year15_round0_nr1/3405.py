f = open('A-large.in')
w = open('output.txt', 'w')
cases = int(f.readline())
for c in range(cases):
  s, a = 0, 0
  m, p = f.readline().split()
  for i in range(int(m) + 1):
    if s < i:
      a += 1
      s += 1
    s += int(p[i])
  w.write("Case #" + str(c + 1) + ": " + str(a) + "\n")