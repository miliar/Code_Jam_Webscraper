from math import pi

from itertools import combinations as p

def surface_area(r1, r2):
    # calculate the surface area of r1 given r2 above it
    sum = r1[1]*2*pi*r1[0]
    sum = sum + flat_area(r1) - flat_area(r2)
    return sum

def compare_area(r, k):
    return 5
    
def flat_area(r):
    return pi*r[0]*r[0]

def generic_function(n, k, pancakes):
    pancakes = p(pancakes, k)
    max_area = 0
    for set in pancakes:

        test_pans = sorted(set, key=lambda x: (-x[0],-x[1]))

        area = test_pans[k-1][0]*2*pi*test_pans[k-1][1]+pi*test_pans[k-1][0]*test_pans[k-1][0]
        if k > 1:
            for r1, r2 in zip(test_pans[:-1], test_pans[1:]):
                area += surface_area(r1, r2) 
                         
        max_area = max(area, max_area)
    
    return max_area
    
value = int(input())  # read a line with a single integer
for i in range(1, value + 1):
    [n, k] = [int(x) for x in input().split(' ')]
    pancakes = []
    for ii in range(n):
        pancakes.append([int(x) for x in input().split(' ')])
    out = generic_function(n, k, pancakes)
    print("Case #{}: {}".format(i, out))

    