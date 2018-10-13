import sys


file = open(sys.argv[1])
T = int(file.readline())

def solve(scores, suprises, p):
  
  if p > 1:
    min_suprise = p + (p - 2) * 2
    min = (p - 1) * 3 + 1
  else:
    min_suprise = p
    min = p
  result = 0
  suprises_left = suprises
  for score in scores:
    if score >= min:
      result += 1
    elif score >= min_suprise and suprises_left > 0:
      result += 1
      suprises_left -= 1
  return result

for i, line in enumerate(file):
  data = line.strip().split(' ')
  googlers, suprises, p = map(int, data[:3])
  scores = map(int, data[3:])
  result = solve(scores, suprises, p)
  print 'Case #' + str(i + 1) + ': ' + str(result)