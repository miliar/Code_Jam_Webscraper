#!/usr/bin/env python3
import sys

def eprint(*args, **kwargs):
#    print(*args, file=sys.stderr, **kwargs)
    pass

def ishappy(pancakes):
    return all(pancake == "+" for pancake in pancakes)

def flip(pancakes, index, k):
    return pancakes[0:index] + "".join('+' if pancake == '-' else '-' for pancake in pancakes[index:index+k]) + pancakes[index+k:]

def solve(pancakes, k, indent="", seen={}, solved={}):
    eprint(indent+str(pancakes))
    eprint(indent+str(seen))
    eprint(indent+str(solved))
    if pancakes in solved:
        eprint(indent+"already solved this chain, returned cached {}".format(solved[pancakes]))
        return solved[pancakes]
    if ishappy(pancakes):
        eprint(indent+"all happy")
        solved[pancakes] = 0
        return 0
    seen[pancakes] = True
    smallest = sys.maxsize
    for index in range(0, len(pancakes) - k + 1):
        pancakes = flip(pancakes, index, k)
        if pancakes in seen and pancakes not in solved:
            eprint(indent+"skipping flip at {}, seen before in this solve".format(index))
            pancakes = flip(pancakes, index, k)
            continue
        eprint(indent+"flipping at {}".format(index))
        solution = solve(pancakes, k, indent+"  ", seen, solved)
        if solution != sys.maxsize:
            smallest = min([smallest, 1 + solution])
            eprint(indent+"min now {}".format(smallest))
        else:
            eprint(indent+"dead end found")
            pass
        pancakes = flip(pancakes, index, k)
    eprint(indent+"solved {} in {}".format(pancakes, smallest))
    solved[pancakes] = smallest
    eprint(indent+str(pancakes))
    eprint(indent+str(seen))
    eprint(indent+str(solved))
    return smallest

t = int(input())
for i in range(1, t + 1):
    pancakes, k = [s for s in input().split(" ")]
    num_pancakes = len(pancakes)
    k = int(k)
    flips = solve(pancakes, k, "", {}, {})

    if flips == sys.maxsize:
        print("Case #{}: IMPOSSIBLE".format(i))
    else:
        print("Case #{}: {}".format(i, flips))
