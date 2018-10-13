import numpy as np
import math


# def intersect(range1, range2):
#     if (range1[0] <= range2[0] and range2[0] <= range1[1]):
#         return (range2[0], )

#     elif (range2[0] <= range1[0] and range1[0] <= range2[1]):
#         return 1
#     elif range1[1] <= range2[0]:  # range 1 comes completely before range2
#         return -1
#     else:
#         return -2


def max_kit(n, p, packages):

    # greedy
    current_package = [0]*n
    num_kit = 0

    

    END = 0

    while not END:
        current_range = [0, math.inf]
        #print(current_range)
        for ingred in range(n):
            while current_package[ingred] < p and (packages[ingred][current_package[ingred]][1] < current_range[0]
                                                  or packages[ingred][current_package[ingred]][1] 
                                                     < packages[ingred][current_package[ingred]][0]):  # if the range is degenerate
                current_package[ingred] += 1

            num = current_package[ingred]

            if num >= p:
                END = 1
                break

            new_range = packages[ingred][num]

            # loop again
            if new_range[0] > current_range[1]:
                current_package[0] += 1
                break

            # intersection range
            current_range = [max(new_range[0], current_range[0]), min(new_range[1], current_range[1])]
            # print(current_range)
            # assert current_range[1] >= current_range[0]

            # we've found a kit; use all current packages
            if ingred == n-1:
                num_kit += 1
                current_package = [i+1 for i in current_package]




    return num_kit


def get_range(x):
    return [math.ceil(x/1.1), math.floor(x/0.9)]


t = int(input())  # read a line with a single integer

for j in range(1, t + 1):
    n, p = map(int, input().split(" "))

    recipe = list(map(int, input().split(" ")))

    packages = list(list(map(lambda x: get_range(x/recipe[i]), sorted(list(map(int, input().split(" ")))))) for i in range(n))  # sort packages by size
       

    #print(n, p, recipe, packages)

    print("Case #{}: {}".format(j, max_kit(n, p, packages)))