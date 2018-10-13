import sys

class Team(object):
  def __init__(self, max_miss):
    self.max_miss = max_miss

  def min_cost(self, misses):
    if misses > self.max_miss:
      return float('inf')
    return 0

class Match(object):
  def __init__(self, cost, left, right):
    self.cost = cost
    self.left = left
    self.right = right
    self.max_miss = min(left.max_miss, right.max_miss)
    self.memoized_costs = dict()
    print >>sys.stderr, "created with max_miss = {0}, cost = {1}".format(self.max_miss, self.cost)

  def _min_cost(self, misses):
    if misses > self.max_miss:
      return float('inf')
    if misses == self.max_miss:
      miss_cost = float('inf')
    else:
      miss_cost = self.left.min_cost(misses + 1) + self.right.min_cost(misses + 1)
    if miss_cost == 0:
      # we can miss the whole tree
      return 0
    see_cost = self.cost + self.left.min_cost(misses) + self.right.min_cost(misses)
    return min(miss_cost, see_cost)
      

  def min_cost(self, misses):
    if misses not in self.memoized_costs:
      self.memoized_costs[misses] = self._min_cost(misses)
    return self.memoized_costs[misses]

if __name__ == '__main__':
  lines = sys.stdin.readlines()
  lines.pop(0)
  case_num = 0
  while lines:
    case_num += 1
    p = int(lines.pop(0))
    ms = map(int, lines.pop(0).split())
    costs = []
    for i in range(p):
      costs.append(map(int, lines.pop(0).split()))
    matches = map(Team, ms)
    while costs:
      next_matches = []
      for c in costs.pop(0):
        next_matches.append(Match(c, matches.pop(0), matches.pop(0)))
      assert not matches
      matches = next_matches
    assert len(matches) == 1
    print "Case #{0}: {1}".format(case_num, matches[0].min_cost(0))

