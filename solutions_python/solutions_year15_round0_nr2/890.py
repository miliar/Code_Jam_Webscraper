import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument('input', type=str, 
                    help='Input file')
args = parser.parse_args()

BRUTE_FORCE_TRIES = 1000


def do_x_times(f, x, *args, **kwargs):
    for _ in range(x):
        f(*args, **kwargs)


def manipulate(pancakes):
    '''Takes a pile at random and move random # of pancakes to a new diner'''
    pancakes.sort(reverse=True)
    if pancakes[0] <= 1:
        return
    rand_ammount = random.randint(1, pancakes[0] - 1)
    pancakes[0] -= rand_ammount
    pancakes.append(rand_ammount) 


def best_after_N_special_minutes(pancakes, special_minutes):
    '''
    Given N special minutes at the beginning, what is
    the remaining time (the max pancakes a diner have)
    '''
    brute_forced_options = []
    for _ in range(BRUTE_FORCE_TRIES):  
        pancakes_case = pancakes[:]
        do_x_times(manipulate, special_minutes, pancakes_case)
        brute_forced_options.append(pancakes_case)
    optimum = min(brute_forced_options, key=max)
    return optimum


assertion = best_after_N_special_minutes([9, 3, 3, 3], 2)
assert assertion == [3, 3, 3, 3, 3, 3]


def solve(pancakes):
    minutes = [max(best_after_N_special_minutes(pancakes, x)) +  x
               for x in range(max(pancakes))]
    return min(minutes)


assertion = solve([9, 3, 3, 3])
assert assertion == 5


with open(args.input) as f:
    cases = int(f.readline().strip())
    for case in range(1, cases + 1):
        f.readline()  # The number of diners is in the array itself
        pancakes = [int(x) for x in f.readline().strip().split()]
        minutes = solve(pancakes)
        print('Case #{}: {}'.format(case, minutes))
