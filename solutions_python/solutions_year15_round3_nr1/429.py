import fileinput
f = fileinput.input()
t = int(f.readline())
for tt in range(1, t+1):
  r,c,w = map(int, f.readline().split())
  print "Case #%d: %d" % (tt, r*((c-1)/w+w))