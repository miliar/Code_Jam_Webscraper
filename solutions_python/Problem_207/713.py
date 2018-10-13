import sys

COLORS = 'ROYGBV'
sys.setrecursionlimit(1100)

ADJACENT = {'R': 'OV', 'O': 'RY', 'Y': 'OG', 'G': 'YB', 'B': 'GV', 'V': 'BG'}

def adjacent(start, target):
  return (start is target) or (target in ADJACENT[start])

def can_be_next(start):
  return [c for c in COLORS if not adjacent(start, c)]

def run():
  test_case_count = int(raw_input())  # read a line with a single integer
  for case in range(1, test_case_count + 1):
    counts_by_color = dict(zip(COLORS, [int(x.strip()) for x in raw_input().split(" ")][1:]))

    solution = solve(counts_by_color)

    print("Case #{}: {}".format(case, solution))

def impossible(counts_by_color):
  biggest = max(counts_by_color, key=lambda c: counts_by_color.get(c, 0))
  return 2 * counts_by_color[biggest] > sum(counts_by_color.values())

def solve(counts_by_color):
  # arbitrarily start with the biggest one
  if impossible(counts_by_color):
    return 'IMPOSSIBLE'

  for color in COLORS:
    if counts_by_color[color] == 0:
      del counts_by_color[color]

  for start_key in sorted(counts_by_color, key=lambda c: counts_by_color.get(c, 0) * -1):
    if counts_by_color.get(start_key, 0) == 0:
      return 'IMPOSSIBLE' # we got to a bad place

    solution = solve_part(start_key, counts_by_color, start_key)
    if solution is not None:
      return "".join(solution)

  return 'IMPOSSIBLE'


def solve_part(cur, counts_by_color, final_key):
  # print counts_by_color
  if sum(counts_by_color.values()) == 0:
    if cur == final_key:
      return [] # dont need to output the last one but glad we tried to find it
    else:
      return None

  next_candidates = can_be_next(cur)

  for candidate in sorted(next_candidates, key=lambda c: counts_by_color.get(c, 0) * -1):
    # print next_candidates, counts_by_color, candidate
    if counts_by_color.get(candidate, 0) == 0:
      # we have exhausted the good options
      return None

    new_counts = dict(counts_by_color)
    new_counts[candidate] -= 1
    if new_counts[candidate] == 0:
      del new_counts[candidate]
    rest_solved = solve_part(candidate, new_counts, final_key)

    if rest_solved is not None:
      return [cur] + rest_solved
    # otherwise keep trying with the other candidates

  return None # no good options

run()
