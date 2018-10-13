#! /usr/bin/env python

MAX_FARMS = 1000000

def main():
    with open('b.in', 'r') as fin, open('b.out', 'w') as fout:
        num_cases = int(fin.readline())
        for case in range(1, num_cases + 1):
            cost, farm_benefit, goal = map(float, fin.readline().split())
            best_time = solve(cost, farm_benefit, goal)
            fout.write('Case #{0}: {1:.7f}\n'.format(case, best_time))
    return

def solve(cost, farm_benefit, goal):
    """Probably won't work on large instance..."""
    initial_rate = current_rate = 2.0
    if cost > goal:
        return goal / current_rate
    best_time = float('inf')
    time = 0
    for num_farms in range(MAX_FARMS):
        time += cost/current_rate
        best_time = min(best_time, time + (goal - cost)/current_rate)
        current_rate += farm_benefit
    return best_time

if __name__ == '__main__':
    main()
