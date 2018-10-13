from math import pi
from queue import PriorityQueue
import itertools


from math import pi
from queue import PriorityQueue
import itertools


def choose_best(combos):
    total_for_best_combo = 0
    for combo in combos:
        largest_radius = 0
        total_edges = 0
        for cake in combo:
            R, H = cake
            total_edges += 2 * pi * R * H
            if R > largest_radius:
                largest_radius = R
        grand_total = total_edges + (largest_radius ** 2 * pi)
        if grand_total > total_for_best_combo:
            total_for_best_combo = grand_total
    return total_for_best_combo
        

input_file = open("A-small-attempt1.in", "r")
output_file = open("A-small-attempt1.out", "w")
T = int(input_file.readline())
print(T)
for t in range(1, T+1):
    N, K = [int(x) for x in input_file.readline().split()]
    cakes = []
    for i in range(N):
        R, H = [int(x) for x in input_file.readline().split()]
        cakes.append((R, H))
    combos = itertools.combinations(cakes, K)
    total_value = choose_best(combos)
    print(total_value)
    output_file.write("Case #{}: {}\n".format(t, total_value))
    
input_file.close()
output_file.close()
print("Files closed")
