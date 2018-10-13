# python2.7. not including shebang, because not sure of remote system setup.

def get_grid_and_answer():
  answer = int(raw_input())
  grid = []
  for i in xrange(4):
    grid.append(map(int, raw_input().split()))
  return grid, answer

T = int(raw_input())
for n in xrange(T):
  grid1, answer1 = get_grid_and_answer()
  grid2, answer2 = get_grid_and_answer()
  print 'Case #' + str(n+1) + ':',
  row1 = set(grid1[answer1-1])
  row2 = set(grid2[answer2-1])
  possible = row1 & row2 # intersect
  if len(possible) > 1:
    print 'Bad magician!'
  elif len(possible) < 1:
    print 'Volunteer cheated!'
  else:
    print next(iter(possible)) # extract single item from set


