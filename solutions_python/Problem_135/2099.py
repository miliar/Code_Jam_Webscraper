import sys

lines = sys.stdin.readlines()

num_cases = int(lines[0])
lines = lines[1:]

def get_grid(lines):
  answer = int(lines[0])
  grid = []
  for i in range(1, 5):
    line = lines[i]
    arr = []
    for c in line.strip().split(' '):
      arr += [int(c)]
    grid += [arr]
  return answer, grid, lines[5:]

print num_cases
for i in range(1, num_cases+1):
  a1, g1, lines = get_grid(lines)
  a2, g2, lines = get_grid(lines)
  
  matches = []
  for c in g1[a1-1]:
    for c2 in g2[a2-1]:
      if c == c2:
        matches += [c]
  if len(matches) == 1:
    print "Case #%s: %s" % (i, matches[0])
  elif len(matches) > 1:
    print "Case #%s: Bad magician!" % i
  else:
    print "Case #%s: Volunteer cheated!" % i

