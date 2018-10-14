f = open('C-small-attempt0.in', 'r')

tofind = "welcome to code jam"

tests = int(f.readline().strip())

# print "num tests: %s" % tests

cnt = 1

## Max Depth: len(looking_for) ... should be ok stackwise
def check_line(looking_for, line):
  if(len(looking_for) == 0):
    # found an occurence, return value and keep searching
    return 1
  total = 0
  let = looking_for[0]
  # print "Cur letter: %s" % let
  for i in range(0, len(line) - len(looking_for) + 1):
    if line[i] == let:
      total += check_line(looking_for[1:], line[i:])
  return total

for line in f:
  line = line.strip()
  ret = check_line(tofind, line)
  print "Case #%d: %.4d" % (cnt, ret)
  cnt += 1
