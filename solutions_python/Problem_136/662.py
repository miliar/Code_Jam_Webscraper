#!/usr/bin/python3

# Dumb method is to step... how many steps is the worst case?
# 1 c/sec, target 10e5

# From current point:
# Evaluate distance to next farm, and distance to goal from current position
# So... generate a tree? Actually it's linear, should be able to just step upwards...

# Dumb approach, blowout case is still only about 2.5 minutes

# Faster approach: Can the time to get to X farms be calculated?
# target / 2.0 for the first one, + target/(2.0 + production),  +target(/2.0+production+production...)
# Nope, can't remember the math

def debug(*args, **kwargs):
    #print(*args, **kwargs)
    pass

cases = int(input())

for case in range (1, cases + 1):
    (cost, production, target) = [float(x) for x in input().split()]

    debug(cost, production, target)
    answer = 0

    generation = 2.0
    best = target / generation
    time = 0.0

    while(True):
        stay = target / generation

        if best < time + stay:
            break

        best = time + stay
        time += cost / generation
        generation += production


    print("Case #%s: %0.7f" % (case, best))
