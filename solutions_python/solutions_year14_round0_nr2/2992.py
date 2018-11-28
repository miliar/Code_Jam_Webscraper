# codejam 2014 : qualifiers
# 2 : cookie cutter
import sys
from itertools import count
from collections import namedtuple

# initial cookie growth
GROWTH = 2.0 # in cookies per second

def define_marginal_factory_gain(raw_gain):
  def marginal_gain(count):
    return 1.0 / (1.0 + (count * raw_gain) / GROWTH)
  return marginal_gain

def solve(cost, gain, target):
  # constants
  base_time = target / GROWTH
  factory_target_relation = cost / target
  marginal_gain = define_marginal_factory_gain(gain)
  # initial
  factory_influence = 0 # cached formula state
  last_time_factor = 1  # time modifier
  # search
  for factory_count in count():
    next_factory_gain = marginal_gain(factory_count)
    time_factor = factory_influence + next_factory_gain
    if (time_factor > last_time_factor):
      break
    factory_influence = factory_influence + (factory_target_relation * next_factory_gain)
    last_time_factor = time_factor
  return base_time * last_time_factor

def parse(input):
  return [float(_) for _ in input.readline().split()]

def main(input):
  case_count = int(input.readline())
  for i in range(1, case_count + 1):
    case = parse(input)
    result = solve(*case)
    print('Case #{0:n}: {1:.7f}'.format(i, result))

if __name__ == '__main__':
  main(sys.stdin)