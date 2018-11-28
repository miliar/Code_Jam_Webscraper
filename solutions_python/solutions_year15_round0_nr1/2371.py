import sys

def additional_needed(mx, levels):
  num_needed = 0
  total = 0
  for i, n in enumerate(levels):
    diff = (i + 1) - n - total
    if diff > 0:
      num_needed += diff
      total += diff
    total += n
  return num_needed

cases = -1
count = 1
for line in sys.stdin:
  if cases == -1:
    cases = int(line.strip())
  else:
    shy_max, shyness = line.strip().split(" ")
    shyness_levels = map(int, shyness)
    print "Case #" + str(count) + ": " + str(additional_needed(shy_max, shyness_levels))
    count += 1
