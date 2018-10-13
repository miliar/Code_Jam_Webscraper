# Calculations
def opera(length, array, index):
  level = 0
  counter = 0
  audience = 0
  for persons in array:
    if level == 0:
      audience += persons
    else:
      if audience >= level:
        audience += persons
      else:
        friends = level - audience
        audience += persons + friends
        counter += friends
    level += 1
  return counter

# Input & Result
for case in range(0, int(input())):
  line = input().split(' '); line = list(filter(bool, line));
  assert len(line) is 2, "och no, wrong input: %r" % line
  print( "Case #%d: %d" % (case + 1, opera(line[0], list(map(int, line[1])), case)) )