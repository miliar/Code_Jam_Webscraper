# Solution to "Freeform Factory" for Google Code Jam 2016
# by Peter Mattsson (quantum.caffeine@gmail.com)
import sys
from copy import deepcopy
from itertools import permutations
from collections import deque

def cases(inputFile):
    with open(inputFile, 'r') as f:
        numCases = int(f.readline())
        for _ in range(numCases):
            n = int(f.readline())
            mapping = [[int(x) for x in f.readline().rstrip('\n')] for _ in xrange(n)]
            yield n, mapping

def innerCheck(mapping, order, assigned, pos):
    if pos == len(order):
        return True
    valid = 0
    for a in (x for x,i in enumerate(mapping[order[pos]]) if i == 1):
        if a in assigned: continue
        if not innerCheck(mapping, order, assigned | set((a,)), pos + 1):
            return False
        else:
            valid += 1
    return valid != 0

def check(mapping):
    workers = len(mapping)
    return all(innerCheck(mapping, order, set(), 0) for order in permutations(range(workers)))

def solve(n, mapping):
    if check(mapping):
        return 0
    options = deque()
    options.append((mapping, 0, 0, 0))
    while options:
        mapping, worker, machine, added = options.popleft()
        while True:
            if mapping[worker][machine] == 0:
                newMap = deepcopy(mapping)
                newMap[worker][machine] = 1
                if check(newMap):
                    return str(added+1)
                machine += 1
                if machine == n:
                    worker += 1
                    machine = 0
                if worker < n:
                    options.append((newMap, worker, machine, added+1))
                else:
                    break
            else:
                machine += 1
                if machine == n:
                    worker += 1
                    machine = 0
                if worker == n:
                    break


with open(sys.argv[2], 'w') as f:
    for num, data in enumerate(cases(sys.argv[1])):
        f.write("Case #%d: %s\n"%(num+1, solve(*data)))
