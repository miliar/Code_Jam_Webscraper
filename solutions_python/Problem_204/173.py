# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def round_up(x):
  if x == int(x):
    return int(x)
  else:
    return int(x + 1)

def ratatouille(N, P, needed_ingredient, ingredient_packages):
  result = 0
  index_tracking = [0] * (N - 1)
  for i in xrange(P):
    candidates = range(round_up(ingredient_packages[0][i] / needed_ingredient[0] / 1.1), int(ingredient_packages[0][i] / needed_ingredient[0] / 0.9) + 1)
    possible = False
    for candidate in candidates:
      is_okay = True
      for j in xrange(1, N):
        index_tracked = index_tracking[j - 1]
        if index_tracked > P - 1:
          is_okay = False
          break
        ingredient_amount = ingredient_packages[j][index_tracked]
        while index_tracked <= P - 1 and ingredient_amount < needed_ingredient[j] * candidate * 0.9:
          index_tracked += 1
          if index_tracked == P:
            is_okay = False
            break
          ingredient_amount = ingredient_packages[j][index_tracked]

        index_tracking[j-1] = index_tracked
        if ingredient_amount > needed_ingredient[j] * candidate * 1.1:
          is_okay = False
          break

      if is_okay:
        result += 1
        for j in xrange(1, N):
          index_tracking[j-1] += 1
        break
  return result


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  N, P = [int(s) for s in raw_input().split(" ")]  
  needed_ingredient = [int(s) for s in raw_input().split(" ")] 
  ingredient_packages = []
  for j in xrange(N):
    ingredient_packages.append(sorted([float(s) for s in raw_input().split(" ")]))

  print "Case #{}: {}".format(i, ratatouille(N, P, needed_ingredient, ingredient_packages))

 # check out .format's specification for more formatting options