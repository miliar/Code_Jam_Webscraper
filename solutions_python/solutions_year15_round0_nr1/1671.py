from sys import stdin

def solve(shyness_map):
  num_standing = 0
  num_added = 0
  for i in range(len(shyness_map)):
    additional_needed = max(i - num_standing, 0)
    num_standing += shyness_map[i] + additional_needed
    num_added += additional_needed
  return num_added

num_cases = int(stdin.readline())
for case_num in range(1, num_cases+1):
  line = stdin.readline().split()
  max_shyness = int(line[0])
  shyness_map = [int(i) for i in line[1]]
  solution = solve(shyness_map)

  print "Case #" + str(case_num) + ": " + str(solution)