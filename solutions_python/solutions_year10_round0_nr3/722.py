#ride

print 'ride'
f = "mytest"
f = 'C-small-attempt1'
#f = 'A-large-practice'
#f = sys.stdin
infile = open(f+".in", "r")
outfile = open(f+".out", "w")

def ReadInts():
  return list(map(int, infile.readline().strip().split(" ")))

T = ReadInts()[0]
for each in range (1, T+1):
  (R, k, N) = ReadInts()
  oq = ReadInts()
  print R, k, N

  t = 0
  q = oq[:]
  for i in range(R):
    l = k
    count = 0
    while len(q) > 0 and q[0] <= l and count < N:
      a = q.pop(0)
      q.append(a)
      l -= a
      count+=1
    t += k-l
    l = k

  print "Case #%d: %d" % (each, t)
  outfile.write("Case #%d: %d\n" % (each, t))
  
