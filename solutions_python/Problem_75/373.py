#!/usr/bin/python
from collections import defaultdict

def update_last_pos(last_pos, car, pos):
  last_pos[car].append(pos)
  if len(last_pos[car]) > 2:
    last_pos[car].pop(0)

def solve(transf, opposite, input):
  start_pos = 0
  last_pos = defaultdict(list)
  ret = []
  for idx, car in enumerate(input):
    if len(ret) == 0:
      ret.append(car)
      update_last_pos(last_pos, car, len(ret) - 1)
    else:
      last_pair = tuple(sorted([ret[-1], car]))
      current_car = car
      # transf
      if transf.has_key(last_pair) and start_pos < len(ret):
        last_pos[ret[-1]].pop(len(last_pos[ret[-1]]) - 1)
        current_car = transf[last_pair]
        ret[len(ret) - 1] = current_car
        update_last_pos(last_pos, current_car, len(ret) - 1)
      else:
        ret.append(car)
        update_last_pos(last_pos, car, len(ret) - 1)
        # remove
        for op in opposite.get(current_car, []):
          if last_pos.has_key(op) and last_pos[op] \
              and last_pos[op][-1] >= start_pos:
            start_pos = len(ret)
            break
  return '[' + ', '.join(ret[start_pos:]) + ']'

def main():
  num_tests = int(raw_input())
  for test in xrange(num_tests):
    comp = raw_input().split()
    transf = {}
    c = int(comp[0])
    for i in xrange(1, c + 1):
      a, b, t = comp[i][0], comp[i][1], comp[i][2]
      transf[tuple(sorted((a, b)))] = t
    d = int(comp[c + 1])
    opposite = defaultdict(list)
    for i in xrange(d):
      a, b = comp[i + c + 1 + 1][0] + comp[i + c + 1 + 1][1]
      opposite[a].append(b)
      opposite[b].append(a)
    n = int(comp[1 + c + 1 + d])
    input = comp[1 + c + 1 + d + 1]
    print "Case #{0}: {1}".format(test + 1,
        solve(transf, opposite, input))

if __name__=="__main__":
  main()
