import math

def parse(input_file, output_file):
    with open(input_file) as f:
        #lines = f.readlines()
        #print(f.readline())
        n_cases = int(f.readline().split()[0])
        data = dict()
        fulls = [0] * n_cases
        for i in range(n_cases):
            fulls[i] = int(f.readline().split()[0])
            data[i] = [int(x) for x in f.readline().split()]
    f = open(output_file, 'w')
    for i in range(n_cases):
        sol = solve(fulls[i], data[i])
        line = "Case #"+str(i+1)+": "+str(sol)
        print(line)
        f.write(line+'\n')
    return

'''
def solve(n_full, pies):
    most_pie = max(pies)
    num_pies = [0] * (most_pie+1)
    for i in pies:
        num_pies[i] += 1
    current_most = most_pie
    current_least_min = most_pie
    spec_min = 0  # number of special minutes used
    while current_most > 2:
        #if current_most == 2:
            #break   #meaning all piles are <= 2
        assert num_pies[current_most] > 0 and current_most > 2
        # now cut the biggest piles in half
        num_pies[current_most//2] += num_pies[current_most]
        num_pies[current_most - current_most//2] += num_pies[current_most]
        spec_min += num_pies[current_most]
        num_pies[current_most] = 0
        while num_pies[current_most] == 0 and current_most > 0:
            current_most -= 1
        min_needed = spec_min + current_most
        current_least_min = min(current_least_min, min_needed)
    return current_least_min
'''

def solve(n_full, pies):
    most_pie = max(pies)
    num_pies = [0] * (most_pie+1)
    for i in pies:
        num_pies[i] += 1
    least_min = most_pie
    for size in range(2, most_pie):  # size of the target piles from 2 to most_pie-1
        min_needed = size  # need size minutes to let them finish eating them
        for i in range(size+1, most_pie+1):  # from pile of size+1 to pile of most_pie
            min_needed += (math.ceil(i/size)-1) * num_pies[i]
            #min_needed += num_pies[i]//size
        least_min = min(least_min, min_needed)
    return least_min



solve(3,[2])
solve(3,[3])
solve(3,[4])
solve(3,[5])
solve(3,[25])
solve(3,[100])
solve(3,[100, 100])
solve(3,[1000])

input_file = 'Btest'
input_file = 'B-small-attempt1.in'
input_file = 'B-large.in'
output_file = 'Boutput'
output_file = 'Boutput1.txt'
output_file = 'Boutput-large.txt'
parse(input_file, output_file)

# compare



