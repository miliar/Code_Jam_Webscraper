# coding=utf-8

from __future__ import (absolute_import, division, generators, nested_scopes,
                        print_function, unicode_literals, with_statement)

from math import ceil, floor

def packages_still_possible(serving_range):
  return bool(min(len(amounts) for amounts in serving_range))

def rat(recipe, packages):
  servings = [[x / portion for x in sorted(amounts)] for portion, amounts in zip(recipe, packages)]
  serving_range = [[[int(ceil(x / 1.1)), int(floor(x / .9))] for x in amounts] for amounts in servings]
  serving_range = [[x for x in amounts if x[0] <= x[1]] for amounts in serving_range]
  num_found = 0
  while packages_still_possible(serving_range):
    package_servings_lower_bound = max(x[0][0] for x in serving_range)
    serving_range = [[x for x in amounts if x[1] >= package_servings_lower_bound] for amounts in serving_range]
    if not packages_still_possible(serving_range):
      return num_found
    package_servings_lower_bound = max(x[0][0] for x in serving_range)
    package_servings_upper_bound = min(x[0][1] for x in serving_range)
    if package_servings_lower_bound <= package_servings_lower_bound:
      num_found += 1
      serving_range = [x[1:] for x in serving_range]
  return num_found
  
  
if __name__ == '__main__':
  num_cases = int(raw_input())
  for case in range(num_cases):
    label = 'case #{}:'.format(case + 1)
    ingredients, packages = [int(x) for x in raw_input().split(' ')]
    recipe = [int(x) for x in raw_input().split(' ')]
    packages = [[int(x) for x in raw_input().split(' ')] for i in range(ingredients)]
    print(label, rat(recipe, packages))
