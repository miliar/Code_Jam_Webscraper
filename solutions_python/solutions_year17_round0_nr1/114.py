def call(n):
  a, w = raw_input().split()
  w = int(w)
  line = [True if i == '+' else False for i in a]
  pos = 0
  flips = 0
  while (pos != len(line) - w + 1):
    if line[pos] == False:
      flips += 1
      for i in range(w):
        line[pos+i] = not line[pos+i]
    pos += 1
  while pos != len(line) and flips != -1:
    if line[pos] == False:
      flips = -1
    pos += 1
  print "Case #" + str(n+1) + ": " + (str(flips) if flips != -1 else "IMPOSSIBLE")
      


t = int(raw_input())
for ii in range(t):
  call(ii)