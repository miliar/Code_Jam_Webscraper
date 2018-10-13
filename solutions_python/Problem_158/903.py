from sys import stdin

def solve(X, R, C):
  if X >= 7:
    return True

  grid_size = R*C
  if grid_size % X != 0:
    return True

  for width in range(1, X+1):
    height = X - width + 1
    if width > R or width > C:
      # Forced orientation
      if height > 1 and (height >= R or height >= C):
        return True
    if (width > R or height > C) and (width > C or height > R):
      return True
  return False

num_cases = int(stdin.readline())
for case_num in range(1, num_cases+1):
  X, R, C = [int(i) for i in stdin.readline().split()]
  if solve(X, R, C):
    solution = "RICHARD"
  else:
    solution = "GABRIEL"

  print "Case #" + str(case_num) + ": " + str(solution)