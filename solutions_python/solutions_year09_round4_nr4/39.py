#HAAHHAHHAA THIS WORKS ONLY FOR SMALL.IN LOLOLLLOLL THIS SUCKS DONT READ IT PLEASE OH GOSH
import math
import collections
from itertools import combinations

def solve(plants):
    # Alright, let's special-case this.
    if len(plants) <= 2:
        return max([r for x, y, r in plants])
    # We KNOW we have three plants now. How lame is my solution?????
    best_pair = min(combinations(plants, 2), key=happiness_factor)
    pair_radius = happiness_factor(best_pair)
    loner = set(plants) - set(best_pair)
    _, _, loner_radius = loner.pop()
    return max(pair_radius, loner_radius)

def happiness_factor(pair):
    'How happy are two plants?'
    a, b = pair
    ax, ay, ar = a
    bx, by, br = b
    dx = ax - bx
    dy = ay - by
    return (math.sqrt(dx ** 2 + dy ** 2) + ar + br) / 2.0

input_file  = 'D-small-attempt0.in'
output_file = 'D-small-attempt0.out.txt'

prob, out = open(input_file), open(output_file, 'w')
cases = int(prob.next().strip())
for i in range(1, cases + 1):
    plant_count = int(prob.next().strip())
    plants = []
    for _ in range(plant_count):
        # Read in the (x, y, r) tuple.
        plant = tuple([int(s) for s in prob.next().strip().split()])
        plants.append(plant)
    solution = solve(plants)
    print 'Case #%d: %.6f' % (i, solution)
    out.write('Case #%d: %.6f\n' % (i, solution))
prob.close()
out.close()
