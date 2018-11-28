import sys

def do_pairs_intersect(pair1, pair2):
  top_left = pair1
  other = pair2
  if (pair1[0] < pair2[0]):
    top_left = pair2
    other = pair1
  if top_left[1] < other[1]:
    return 1
  return 0

filename = sys.argv[1]

infile = open(filename)

T = int(infile.readline())

for x in range(T):
  sys.stdout.write("Case #")
  sys.stdout.write(str(x+1))
  sys.stdout.write(": ")
  
  N = int(infile.readline())
  
  wires = {}
  
  for n in range(N):
    pair = [int(v) for v in infile.readline().split()]
    wires[n] = pair
  
  intersections = 0
  
  for n in range(N-1):
    for m in range(n+1, N):
      intersections += do_pairs_intersect(wires[n], wires[m])
      
  print intersections

infile.close()