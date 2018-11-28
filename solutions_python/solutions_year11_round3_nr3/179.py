import sys
filename = 'input.txt'
if len(sys.argv) > 1:
  filename = sys.argv[1]
f = open(filename)
lines = f.readlines()
f.close()
lines = [line.strip() for line in lines]

def solve(l, h, freqs):
  for x in range(l, h+1):
    ok_freq = True
    for freq in freqs:
      if x % freq==0 or freq % x==0:
        continue
      else:
        ok_freq = False
        break
    if ok_freq:
      return x
    
  return 'NO'

N = int(lines[0])
lines = lines[1:]
for i in range(N):
  nlh = lines[0].split(' ')
  n = int(nlh[0])
  l = int(nlh[1])
  h = int(nlh[2])
  lines = lines[1:]
  freqs = lines[0]
  freqs = [int(x) for x in lines[0].split(' ')]
  lines = lines[1:]

  soln = solve(l, h, freqs)
  print "Case #%s: %s" % (i+1, soln)
