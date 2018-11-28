import copy
import sys
from pprint import pprint
from copy import deepcopy

input = file(sys.argv[1])
count = int(input.readline())
i = 1

def calcCost(old, new):
    cost = len(new)
    for i in range(min(len(old), len(new))):
        if old[i] == new[i]:
            cost -= 1
        else:
            break
    return cost
    
while i <= count:
    existing, new = map(int, input.readline().split())
    existing_dirs = [['']]
    new_dirs = []
    for ignore in range(existing):
        existing_dirs.append(input.readline().strip().split('/'))
    for ignore in range(new):
        new_dirs.append(input.readline().strip().split('/'))
    existing_dirs.sort()
    total_costs = 0
    for new_dir in new_dirs:
        cheapest = 10000
        found = False
        for index, old_dir in enumerate(existing_dirs):
            cost = calcCost(old_dir, new_dir)
            if cost < cheapest:
                cheapest = cost
            if cost > cheapest:
                break
                found = True
        total_costs += cheapest
        if cheapest == 0:
            continue
        existing_dirs.append(new_dir)
        existing_dirs.sort()

    orig_dirs = deepcopy(existing_dirs)
    existing_dirs.sort()
    assert orig_dirs == existing_dirs
    
    result = str(total_costs)
    print 'Case #%i: %s' % (i, result)
    i += 1
